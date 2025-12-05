"""
环境配置管理
"""

import os
from pathlib import Path
from typing import Literal


class Config:
    """应用配置类"""
    
    def __init__(self):
        self._load_env()
        
    def _load_env(self):
        """加载 .env 文件"""
        env_file = Path(__file__).parent / '.env'
        
        if env_file.exists():
            with open(env_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # 跳过注释和空行
                    if not line or line.startswith('#'):
                        continue
                    
                    # 解析键值对
                    if '=' in line:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        
                        # 设置环境变量（如果尚未设置）
                        if key and not os.getenv(key):
                            os.environ[key] = value
    
    @property
    def env(self) -> Literal['development', 'production']:
        """获取环境模式"""
        return os.getenv('ENV', 'development')
    
    @property
    def is_development(self) -> bool:
        """是否为开发环境"""
        return self.env == 'development'
    
    @property
    def is_production(self) -> bool:
        """是否为生产环境"""
        return self.env == 'production'
    
    @property
    def debug(self) -> bool:
        """是否开启调试模式"""
        return os.getenv('DEBUG', 'true').lower() in ('true', '1', 'yes')
    
    @property
    def frontend_port(self) -> int:
        """前端服务端口"""
        return int(os.getenv('FRONTEND_PORT', '9696'))
    
    @property
    def frontend_url(self) -> str:
        """前端服务 URL"""
        return os.getenv('FRONTEND_URL', f'http://localhost:{self.frontend_port}')
    
    @property
    def window_width(self) -> int:
        """窗口宽度"""
        return int(os.getenv('WINDOW_WIDTH', '1280'))
    
    @property
    def window_height(self) -> int:
        """窗口高度"""
        return int(os.getenv('WINDOW_HEIGHT', '720'))
    
    @property
    def window_min_width(self) -> int:
        """窗口最小宽度"""
        return int(os.getenv('WINDOW_MIN_WIDTH', '1024'))
    
    @property
    def window_min_height(self) -> int:
        """窗口最小高度"""
        return int(os.getenv('WINDOW_MIN_HEIGHT', '600'))
    
    def get_window_title(self) -> str:
        """获取窗口标题"""
        title = "桌面端应用模板"
        if self.is_development:
            title += " [开发模式]"
        return title
    
    def print_config(self):
        """打印当前配置"""
        print("="*50)
        print("📋 当前配置:")
        print(f"   环境模式: {self.env}")
        print(f"   调试模式: {'开启' if self.debug else '关闭'}")
        print(f"   前端地址: {self.frontend_url}")
        print(f"   窗口尺寸: {self.window_width}x{self.window_height}")
        print("="*50)


# 创建全局配置实例
config = Config()
