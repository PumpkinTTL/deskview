import webview
import subprocess
import os
import time
import requests
import threading
import socket
import atexit
import signal
from datetime import datetime


# 全局变量存储前端进程
frontend_process = None


class API:
    """PyWebView API - 提供前端调用的 Python 接口"""
    
    def __init__(self):
        self.data = {"message": "API 已初始化"}
        print("✅ PyWebView API 已加载")
    
    def say_hello(self, name):
        """测试方法：打招呼"""
        message = f"你好，{name}！当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        print(f"📣 {message}")
        return {
            "success": True,
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_system_info(self):
        """获取系统信息"""
        import platform
        info = {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "python_version": platform.python_version(),
        }
        print(f"💻 系统信息: {info['system']} {info['release']}")
        return {
            "success": True,
            "data": info
        }
    
    def resize_window(self, width, height):
        """调整窗口大小"""
        try:
            # 这个方法需要在窗口创建后通过 window 对象调用
            print(f"🔧 请求调整窗口大小: {width}x{height}")
            return {
                "success": True,
                "message": f"窗口大小已调整为 {width}x{height}"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"调整窗口失败: {str(e)}"
            }
    
    def test_notification(self, title, message):
        """测试通知功能"""
        print(f"🔔 通知 [{title}]: {message}")
        return {
            "success": True,
            "message": "通知已发送"
        }
    
    def run_shell_command(self, command):
        """执行 Shell 命令（谨慎使用）"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            print(f"⚙️ 执行命令: {command}")
            return {
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"命令执行失败: {str(e)}"
            }


def check_port_in_use(port):
    """检查端口是否被占用"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('localhost', port))
            return False  # 端口未被占用
        except OSError:
            return True  # 端口已被占用


def run_frontend():
    """在前端目录中启动 pnpm dev"""
    global frontend_process
    
    frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "frontend"))
    print(f"🚀 正在 {frontend_path} 中启动前端服务...")
    
    # 保存进程引用以便后续关闭
    frontend_process = subprocess.Popen(
        "pnpm dev", 
        cwd=frontend_path, 
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    print(f"✅ 前端进程已启动 (PID: {frontend_process.pid})")


def stop_frontend():
    """停止前端服务"""
    global frontend_process
    
    if frontend_process:
        print("🛑 正在关闭前端服务...")
        try:
            # Windows 下需要使用 taskkill 来终止进程树
            if os.name == 'nt':
                subprocess.run(
                    f"taskkill /F /T /PID {frontend_process.pid}",
                    shell=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            else:
                frontend_process.terminate()
                frontend_process.wait(timeout=5)
            
            print("✅ 前端服务已关闭")
            frontend_process = None
        except Exception as e:
            print(f"⚠️ 关闭前端服务时出错: {e}")


def cleanup():
    """清理资源"""
    stop_frontend()


def wait_for_frontend_ready(url, timeout=30):
    """等待前端服务启动成功"""
    print("⏳ 正在等待前端服务启动...")
    for i in range(timeout):
        try:
            res = requests.get(url, timeout=2)
            if res.status_code == 200:
                print(f"✅ 前端服务已就绪: {url}")
                return True
        except:
            pass
        print(f"   等待中... ({i+1}/{timeout})")
        time.sleep(1)
    
    print("❌ 前端服务启动失败，请检查 pnpm 是否正确执行。")
    return False


if __name__ == "__main__":
    url = "http://localhost:9696"
    port = 9696
    
    print("="*50)
    print("🎯 桌面端应用启动中...")
    print("="*50)
    
    # 注册清理函数
    atexit.register(cleanup)
    
    # 检查端口是否已被占用
    if check_port_in_use(port):
        print(f"✅ 检测到端口 {port} 已开启，跳过启动前端服务")
        # 验证服务是否可访问
        if not wait_for_frontend_ready(url, timeout=5):
            print(f"⚠️ 端口 {port} 已占用但服务不可访问，尝试启动新的前端服务...")
            run_frontend()
            if not wait_for_frontend_ready(url):
                print("\n❌ 前端服务启动失败，请检查端口占用情况")
                input("按回车键退出...")
                exit(1)
    else:
        print(f"🚀 端口 {port} 未占用，启动前端服务...")
        run_frontend()
        
        # 等待前端就绪
        if not wait_for_frontend_ready(url):
            print("\n❌ 前端服务未能启动，请手动运行 'cd frontend && pnpm dev'")
            cleanup()
            input("按回车键退出...")
            exit(1)
    
    # 接入后端 API
    api = API()
    
    # 创建窗口
    print("\n🪟 创建桌面窗口...")
    window = webview.create_window(
        title="桌面端应用模板",
        url=url,
        width=1280,
        height=720,
        resizable=True,
        js_api=api,
        min_size=(1024, 600),
    )
    
    print("✨ 应用启动成功！")
    print("="*50)
    
    try:
        # 启动 GUI
        webview.start(debug=True)
    finally:
        # 窗口关闭后清理资源
        print("\n🔄 应用正在关闭...")
        cleanup()
        print("👋 应用已完全退出")
