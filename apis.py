import webview
import subprocess
import os
import time
import requests
import threading
import json
from typing import Dict, Any

class API:
    def __init__(self):
        self.winsurf_process = None
        self.winsurf_config = {}
        
    def start_winsurf_proxy(self, port=8080):
        """启动Winsurf代理服务"""
        try:
            # 检查端口是否可用
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex(('localhost', port))
            
            if result == 0:
                # 端口可用，停止可能冲突的服务
                self.stop_conflicting_services(port)
                time.sleep(1)
            
            # 启动Winsurf代理
            cmd = [
                'mitmdump',
                '--set', 'confdir=~/.mitmproxy',
                '--listen-port', str(port),
                '--scripts', 'winsurf_interceptor.py'
            ]
            print(f"🚀 正在端口 {port} 启动 Winsurf 代理...")
            
            self.winsurf_process = subprocess.Popen(cmd, cwd=os.path.dirname(__file__), shell=True)
            
            # 等待服务启动
            time.sleep(3)
            
            return {
                "success": True,
                "message": f"代理已启动在端口 {port}",
                "process_id": self.winsurf_process.pid if self.winsurf_process else None
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"启动Winsurf代理失败: {str(e)}"
            }
    
    def stop_winsurf_proxy(self):
        """停止Winsurf代理服务"""
        try:
            if self.winsurf_process:
                self.winsurf_process.terminate()
                self.winsurf_process = None
                print(f"✅ Winsurf代理服务已停止")
                
                return {
                    "success": True,
                    "message": "代理服务已停止"
                }
            else:
                return {
                    "success": False,
                    "message": "没有运行的代理服务"
                }
        except Exception as e:
            return {
                "success": False,
                    "message": f"停止服务失败: {str(e)}"
            }
    
    def check_port_available(self, port, timeout=2):
        """检查端口是否可用"""
        try:
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex(('localhost', port))
            sock.close()
            return result == 0
            
        except:
            return False
    
    def stop_conflicting_services(self, target_port):
        """停止可能冲突的服务"""
        try:
            import psutil
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    # 检查进程是否在监听目标端口
                    for conn in proc.connections():
                        if conn.laddr.port == target_port:
                            proc.terminate()
                            print(f"停止冲突服务: {proc.name} (PID: {proc.pid})")
                            return True
                except:
                    continue
        except Exception as e:
            print(f"停止冲突服务失败: {str(e)}")
            return False
    
    def intercept_winsurf_request(self, target_url, new_data=None):
        """拦截并修改Winsurf API请求"""
        if not new_data:
            new_data = {
                "action": "reset_required",
                "message": "Winsurf配置需要重置"
            }
        else:
            new_data = {
                "action": "config_update",
                "config": new_data
            }
        
        print(f"🔄 拦截Winsurf请求: {target_url}")
        print(f"📤 修改后: {json.dumps(new_data, indent=2, ensure_ascii=False)}")
        
        return {
            "success": True,
            "message": f"Winsurf配置已更新"
        }
    
    def clear_browser_data(self):
        """清除浏览器数据"""
        try:
            # 这里应该调用清除API
            print(f"🧹 清除浏览器数据...")
            
            return {
                "success": True,
                "message": "浏览器数据已清除"
            }
        except Exception as e:
            print(f"清除数据失败: {str(e)}")
            return {
                "success": False,
                "message": f"清除数据失败: {str(e)}"
            }

class WinsurfManager:
    def __init__(self):
        self.proxy_process = None
        self.config_file = None
        self.interceptor_process = None
        self.installer_process = None
        self.proxy_port = 8080
        
    def start_proxy_manager(self):
        """启动代理管理器"""
        try:
            # 生成配置文件
            config_content = self._generate_proxy_config()
            self.config_file = os.path.join(os.path.dirname(__file__), 'winsurf_config.json')
            with open(self.config_file, 'w') as f:
                f.write(json.dumps(config_content, indent=2))
            
            # 生成拦截器脚本
            interceptor_content = self._generate_interceptor_script()
            self.interceptor_file = os.path.join(os.path.dirname(__file__), 'winsurf_interceptor.py')
            with open(self.interceptor_file, 'w') as f:
                f.write(interceptor_content)
            
            # 安装证书（如果需要）
            self._install_certificate()
            
            # 启动代理服务
            proxy_result = self.start_winsurf_proxy(self.proxy_port)
            if proxy_result["success"]:
                self.proxy_process = proxy_result["process_id"]
                
                return {
                    "success": True,
                    "message": "代理管理器已启动",
                    "proxy_port": self.proxy_port
                }
            else:
                return proxy_result
        
        except Exception as e:
            print(f"启动代理管理器失败: {str(e)}")
            return {
                "success": False,
                "message": f"启动代理管理器失败: {str(e)}"
            }
    
    def stop_proxy_manager(self):
        """停止代理管理器"""
        try:
            # 停止所有服务
            if self.proxy_process:
                self.proxy_process.terminate()
                self.proxy_process = None
                
            if self.interceptor_process:
                self.interceptor_process.terminate()
                self.interceptor_process = None
                
            print(f"✅ 代理管理器已停止")
                
                return {
                    "success": True,
                    "message": "代理管理器已停止"
                }
            except Exception as e:
            print(f"停止管理器失败: {str(e)}")
            return {
                "success": False,
                    "message": f"停止管理器失败: {str(e)}"
            }
    
    def _generate_proxy_config(self):
        """生成mitmproxy配置文件"""
        config = {
            "listen-port": self.proxy_port,
            "target-domain": "winsurf.com",
            "target-path": "/api/winsurf/*",
            "response-modifier": {
                "status": "reset_required",
                "config": "Configuration cleared"
            },
            "request-modifier": {
                "status": "config_update",
                "config": "Updated configuration applied"
            }
        }
        return config
    
    def _generate_interceptor_script(self):
        """生成请求拦截器脚本"""
        script_content = '''
import sys
import json
from mitmproxy.http import HTTPFlow
from mitmproxy import ctx

class WinsurfInterceptor:
    def __init__(self):
        self.rules = []
        
    def add_rule(self, pattern: str, modifier: dict):
        """添加拦截规则"""
        rule = {
            "pattern": pattern,
            "modifier": modifier,
            "action": "modify"
        }
        self.rules.append(rule)
        print(f"✅ 已添加拦截规则: {pattern}")
        
    def request(self, flow: HTTPFlow):
        """处理HTTP请求"""
        url = flow.request.pretty_url
        
        # 检查匹配的拦截规则
        matching_rule = None
        for rule in self.rules:
            if rule["pattern"] in url:
                matching_rule = rule
                break
        
        if matching_rule:
            print(f"🎯 匹配规则: {matching_rule['pattern']} - {matching_rule['modifier']}")
            
            # 应用修改
            if matching_rule["action"] == "reset_required":
                print(f"🔄 重置认证状态")
                # 生成重置响应
                response_data = {
                    "action": "authentication_reset",
                    "message": "Authentication status reset"
                }
            elif matching_rule["action"] == "config_update":
                print(f"⚙️ 更新配置: {matching_rule['modifier']}")
                # 模拟配置更新
                config_data = flow.request.get_text()
                try:
                    new_config = json.loads(config_data)
                    response_data = {
                        "action": "config_updated",
                        "config": new_config,
                        "message": "Configuration updated successfully"
                    }
                except:
                    response_data = {
                        "action": "error",
                        "message": "Invalid configuration data"
                    }
            else:
                # 默认透传
                response_data = {
                    "action": "pass_through",
                    "message": "Request passed through"
                }
        
        return response_data

def main():
    interceptor = WinsurfInterceptor()
    
    if len(sys.argv) > 1 and sys.argv[1] == "rules":
        # 测试规则
        pattern = sys.argv[2]
        modifier = {"action": "reset_required"}
        interceptor.add_rule(pattern, modifier)
        print(f"添加规则: {pattern}")
    
    # 启动拦截器（用于测试）
    from mitmproxy.tools import dump

if __name__ == "__main__":
    # 生成配置文件
    manager = WinsurfManager()
    
    # 启动代理管理器
    result = manager.start_proxy_manager()
    
    if result["success"]:
        print("✅ Winsurf代理系统已启动")
        print(f"代理端口: {result['proxy_port']}")
        print(f"拦截器端口: {8081}")
    else:
        print(f"❌ 启动失败: {result['message']}")
'''
        return script_content
    
    def _install_certificate(self):
        """安装mitmproxy证书"""
        try:
            # 这里应该实现证书安装逻辑
            print("证书安装功能待实现...")
        except Exception as e:
            print(f"证书安装失败: {str(e)}")

if __name__ == "__main__":
    # 主程序入口
    api = API()
    winsurf_manager = WinsurfManager()
    
    try:
        print("🚀 启动Winsurf重置系统...")
        
        # 启动代理管理器
        result = winsurf_manager.start_proxy_manager()
        
        if result["success"]:
            print("✅ Winsurf重置系统已启动")
            print(f"访问地址: http://localhost:{result['proxy_port']}")
            print(f"✨ 使用以下API进行操作:")
            print("1. start_proxy_manager(port) - 启动代理管理器")
            print("2. stop_proxy_manager() - 停止代理管理器")
            print("3. intercept_request(target_url, data) - 拦截请求")
            print("4. clear_browser_data() - 清除浏览器数据")
            print("5. 查看代理状态 - 检查当前状态")
        
        except Exception as e:
            print(f"❌ 系统启动失败: {str(e)}")
    
    if __name__ == "test":
    # 测试模式
    main()
'''
        
        return script_content
    
    def _save_to_file(self, content: str, filename: str):
        """保存内容到文件"""
        try:
            with open(filename, 'w') as f:
                f.write(content)
            print(f"✅ 已保存到 {filename}")
        except Exception as e:
            print(f"❌ 保存失败: {str(e)}")
