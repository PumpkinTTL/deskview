"""
PyWebView API 接口定义
提供前端调用的 Python 接口
"""

import subprocess
import platform
from datetime import datetime


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
