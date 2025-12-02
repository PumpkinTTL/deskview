# DeskView

一个基于Python后端和Vue前端的桌面应用程序模板。

## 项目结构

```
deskview/
├── main.py              # 主程序入口，启动PyWebView桌面应用
├── apis.py              # API接口定义，包含Winsurf代理管理功能
├── requirements.txt     # Python依赖包列表
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
- ✅ Winsurf代理管理（可选）
- ✅ 热重载开发环境

## 开发说明

### 前端开发

前端项目位于`frontend/`目录，使用Vue 3 + TypeScript + Vite开发。

主要文件：
- `src/App.vue`: 主应用组件
- `src/views/Home.vue`: 首页组件
- `src/apis/user.ts`: 用户相关API
- `src/utils/`: 工具函数

### 后端开发

后端API定义在`apis.py`中，提供以下功能：
- 系统信息获取
- 窗口操作
- 命令执行
- 代理管理

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
