import webview
import subprocess
import os
import time
import requests
import socket
import atexit
from apis import API
from config import config


# 全局变量存储前端进程
frontend_process = None


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
    # 使用配置文件
    url = config.frontend_url
    port = config.frontend_port
    
    print("="*50)
    print("🎯 桌面端应用启动中...")
    print("="*50)
    
    # 打印配置信息
    config.print_config()
    
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
        title=config.get_window_title(),
        url=url,
        width=config.window_width,
        height=config.window_height,
        resizable=True,
        js_api=api,
        min_size=(config.window_min_width, config.window_min_height),
    )
    
    print("✨ 应用启动成功！")
    print("="*50)
    
    try:
        # 启动 GUI（根据配置决定是否开启调试模式）
        webview.start(debug=config.debug)
    finally:
        # 窗口关闭后清理资源
        print("\n🔄 应用正在关闭...")
        cleanup()
        print("👋 应用已完全退出")
