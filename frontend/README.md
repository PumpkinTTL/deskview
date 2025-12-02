# Vue3 项目模板

基于 Vue3 + TypeScript + Vite 的现代化前端项目模板，集成了完整的开发工具链。

## 🚀 技术栈

- **框架**: Vue 3 + TypeScript
- **构建工具**: Vite
- **UI组件库**: Element Plus (完全自动按需导入)
- **状态管理**: Pinia
- **路由**: Vue Router
- **HTTP客户端**: Axios
- **样式**: SCSS
- **图标**: Font Awesome + Element Plus Icons
- **动画**: Animate.css
- **加密**: JSEncrypt
- **浏览器指纹**: FingerprintJS
- **包管理**: pnpm

## 📦 功能特性

- ✅ Element Plus 组件/图标/API 完全自动按需导入
- ✅ Vue3 Composition API 自动导入
- ✅ TypeScript 支持
- ✅ 路径别名 (@/ 指向 src/)
- ✅ SCSS 全局变量配置
- ✅ Axios 请求/响应拦截器
- ✅ Pinia 状态管理示例
- ✅ Vue Router 路由配置
- ✅ Font Awesome 图标按需导入
- ✅ 浏览器指纹获取
- ✅ RSA 加密工具

## 🛠️ 开发

```bash
# 安装依赖
pnpm install

# 启动开发服务器
pnpm dev

# 构建生产版本
pnpm build

# 预览生产构建
pnpm preview
```

## 📁 项目结构

```
src/
├── apis/           # API 接口
├── assets/         # 静态资源
├── components/     # 公共组件
├── router/         # 路由配置
├── store/          # Pinia 状态管理
├── styles/         # 样式文件
├── types/          # 类型声明
├── utils/          # 工具函数
├── views/          # 页面组件
├── App.vue         # 根组件
└── main.ts         # 入口文件
```

## 🔧 配置说明

### Vite 配置
- Element Plus 自动导入
- Vue/Pinia/Vue Router API 自动导入
- 路径别名配置
- SCSS 全局变量

### TypeScript 配置
- 严格模式
- 路径映射
- 自动导入类型声明

### 样式配置
- SCSS 预处理器
- Element Plus 主题变量
- 全局样式变量

## 📖 使用示例

### Element Plus 组件使用
```vue
<template>
  <!-- 无需导入，自动按需加载 -->
  <el-button type="primary">按钮</el-button>
  <el-input v-model="value" />
</template>
```

### Font Awesome 图标使用
```vue
<template>
  <font-awesome-icon :icon="['fas', 'user']" />
</template>
```

### Pinia 状态管理
```ts
// 自动导入，无需手动导入
const store = useCounterStore()
const { count } = storeToRefs(store)
```

### API 请求
```ts
import { getUserInfo } from '@/apis/user'

const user = await getUserInfo()
```
