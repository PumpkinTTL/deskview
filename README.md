# DeskView

一个基于Python后端和Vue前端的桌面应用程序模板。

## 项目结构

```
deskview/
├── main.py              # 主程序入口，启动PyWebView桌面应用
├── apis.py              # API接口定义
├── config.py            # 环境配置管理
├── requirements.txt     # Python依赖包列表
├── .env                 # 环境变量配置（不提交到Git）
├── .env.example         # 环境变量配置示例
├── .env.production      # 生产环境配置示例
├── .gitignore          # Git忽略文件配置
├── frontend/           # Vue.js前端项目
│   ├── src/           # 前端源代码
│   ├── package.json   # 前端依赖配置
│   └── vite.config.ts # Vite构建配置
└── README.md          # 项目说明文档
```

## 技术栈

### 后端
- **Python**: 主要编程语言
- **PyWebView**: 创建桌面应用窗口
- **Requests**: HTTP请求处理
- **psutil**: 系统进程管理

### 前端
- **Vue.js 3**: 前端框架
- **TypeScript**: 类型安全的JavaScript
- **Vite**: 快速构建工具
- **pnpm**: 包管理器

## 快速开始

### 环境要求

- Python 3.8+
- Node.js 16+
- pnpm (推荐) 或 npm

### 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/PumpkinTTL/deskview.git
   cd deskview
   ```

2. **设置Python虚拟环境**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **安装Python依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **安装前端依赖**
   ```bash
   cd frontend
   pnpm install
   cd ..
   ```

5. **配置环境变量**
   ```bash
   # 复制环境配置文件
   cp .env.example .env
   
   # 根据需要修改 .env 文件
   # ENV=development  # 开发环境
   # ENV=production   # 生产环境
   ```

### 运行应用

1. **启动应用**
   ```bash
   python main.py
   ```

2. **或分别启动前后端**

   启动前端开发服务器：
   ```bash
   cd frontend
   pnpm dev
   ```

   然后启动Python后端：
   ```bash
   python main.py
   ```

## 功能特性

- ✅ 桌面应用程序窗口
- ✅ 前后端通信API
- ✅ 系统信息获取
- ✅ 窗口大小调整
- ✅ Shell命令执行
- ✅ 通知功能
- ✅ 环境配置管理（开发/生产）
- ✅ 智能端口检测
- ✅ 进程生命周期管理
- ✅ 热重载开发环境

## 环境配置

项目使用 `.env` 文件管理环境配置，支持开发和生产环境切换。

### 配置项说明

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `ENV` | 环境模式 (development/production) | development |
| `DEBUG` | 调试模式 (true/false) | true |
| `FRONTEND_PORT` | 前端服务端口 | 9696 |
| `FRONTEND_URL` | 前端服务地址 | http://localhost:9696 |
| `WINDOW_WIDTH` | 窗口宽度 | 1280 |
| `WINDOW_HEIGHT` | 窗口高度 | 720 |
| `WINDOW_MIN_WIDTH` | 窗口最小宽度 | 1024 |
| `WINDOW_MIN_HEIGHT` | 窗口最小高度 | 600 |

### 切换环境

**开发环境**
```bash
# .env 文件
ENV=development
DEBUG=true
```

**生产环境**
```bash
# .env 文件
ENV=production
DEBUG=false
```

或者直接复制对应的配置文件：
```bash
# 使用生产环境配置
cp .env.production .env
```

## 开发说明

### 前端开发

前端项目位于`frontend/`目录，使用Vue 3 + TypeScript + Vite开发。

主要文件：
- `src/App.vue`: 主应用组件
- `src/views/Home.vue`: 首页组件
- `src/components/ApiTest.vue`: API测试组件
- `src/utils/`: 工具函数

### 后端开发

后端API定义在`apis.py`中，提供以下功能：
- 系统信息获取
- 窗口操作
- 命令执行
- 通知功能

配置管理在`config.py`中，支持：
- 环境变量加载
- 配置项访问
- 环境判断

## 部署说明

### 开发环境
运行`python main.py`即可启动开发版本。

### 生产环境
1. 构建前端：`cd frontend && pnpm build`
2. 修改`main.py`中的URL指向构建后的文件
3. 使用PyInstaller等工具打包为可执行文件

## 贡献指南

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/AmazingFeature`
3. 提交更改：`git commit -m 'Add some AmazingFeature'`
4. 推送到分支：`git push origin feature/AmazingFeature`
5. 提交Pull Request

## 许可证

本项目采用MIT许可证，详情请查看[LICENSE](LICENSE)文件。

## 联系方式

- 项目链接：[https://github.com/PumpkinTTL/deskview](https://github.com/PumpkinTTL/deskview)
- 作者：PumpkinTTL
