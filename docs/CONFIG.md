# 环境配置指南

## 概述

DeskView 使用 `.env` 文件管理环境配置，支持灵活的开发和生产环境切换。

## 配置文件

### .env
实际使用的配置文件（不会提交到 Git）

### .env.example
配置文件模板，包含所有可用的配置项

### .env.production
生产环境配置示例

## 配置项详解

### ENV
- **类型**: string
- **可选值**: `development` | `production`
- **默认值**: `development`
- **说明**: 环境模式，影响窗口标题显示和调试行为

### DEBUG
- **类型**: boolean
- **可选值**: `true` | `false`
- **默认值**: `true`
- **说明**: 是否开启 PyWebView 调试模式，开启后可以使用开发者工具

### FRONTEND_PORT
- **类型**: number
- **默认值**: `9696`
- **说明**: 前端开发服务器端口

### FRONTEND_URL
- **类型**: string
- **默认值**: `http://localhost:9696`
- **说明**: 前端服务完整地址

### WINDOW_WIDTH / WINDOW_HEIGHT
- **类型**: number
- **默认值**: `1280` / `720`
- **说明**: 应用窗口初始尺寸

### WINDOW_MIN_WIDTH / WINDOW_MIN_HEIGHT
- **类型**: number
- **默认值**: `1024` / `600`
- **说明**: 应用窗口最小尺寸限制

## 使用示例

### 开发环境配置

```env
ENV=development
DEBUG=true
FRONTEND_PORT=9696
FRONTEND_URL=http://localhost:9696
WINDOW_WIDTH=1280
WINDOW_HEIGHT=720
WINDOW_MIN_WIDTH=1024
WINDOW_MIN_HEIGHT=600
```

### 生产环境配置

```env
ENV=production
DEBUG=false
FRONTEND_PORT=9696
FRONTEND_URL=http://localhost:9696
WINDOW_WIDTH=1280
WINDOW_HEIGHT=720
WINDOW_MIN_WIDTH=1024
WINDOW_MIN_HEIGHT=600
```

## 在代码中使用配置

### Python 后端

```python
from config import config

# 判断环境
if config.is_development:
    print("开发环境")

if config.is_production:
    print("生产环境")

# 获取配置值
port = config.frontend_port
debug = config.debug
url = config.frontend_url

# 获取窗口配置
width = config.window_width
height = config.window_height
```

### 配置类方法

```python
# 打印当前配置
config.print_config()

# 获取窗口标题（自动添加环境标识）
title = config.get_window_title()
# 开发环境: "桌面端应用模板 [开发模式]"
# 生产环境: "桌面端应用模板"
```

## 最佳实践

1. **不要提交 .env 文件**
   - `.env` 文件已在 `.gitignore` 中
   - 每个开发者可以有自己的配置

2. **使用 .env.example 作为模板**
   - 新成员克隆项目后复制此文件
   - 包含所有必需的配置项

3. **生产环境关闭调试**
   - 设置 `DEBUG=false`
   - 设置 `ENV=production`

4. **端口冲突处理**
   - 如果 9696 端口被占用，修改 `FRONTEND_PORT`
   - 同时更新 `FRONTEND_URL`

## 故障排查

### 配置未生效
1. 检查 `.env` 文件是否存在
2. 确认配置项格式正确（无多余空格）
3. 重启应用使配置生效

### 端口冲突
1. 修改 `.env` 中的 `FRONTEND_PORT`
2. 或使用应用的智能端口检测功能

### 窗口尺寸异常
1. 检查 `WINDOW_WIDTH` 和 `WINDOW_HEIGHT` 值
2. 确保不小于最小尺寸限制
