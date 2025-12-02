# Font Awesome 图标配置说明

## ✅ 已修复的问题

之前遇到的 `Could not find one or more icon(s) {prefix: 'fas', iconName: 'plus'}` 错误已经解决。

## 🔧 配置步骤

### 1. 安装依赖
```bash
pnpm add @fortawesome/fontawesome-svg-core @fortawesome/free-solid-svg-icons @fortawesome/vue-fontawesome
```

### 2. 在 main.ts 中配置
```typescript
// Font Awesome 图标
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { 
  faUser, faLock, faHome, faCog, faPlus, faMinus, faRefresh,
  faSearch, faEdit, faTrash, faSave, faCheck, faTimes,
  faEye, faEyeSlash, faDownload, faUpload, faArrowLeft, faArrowRight
} from '@fortawesome/free-solid-svg-icons'

// 添加图标到库
library.add(
  faUser, faLock, faHome, faCog, faPlus, faMinus, faRefresh,
  faSearch, faEdit, faTrash, faSave, faCheck, faTimes,
  faEye, faEyeSlash, faDownload, faUpload, faArrowLeft, faArrowRight
)

// 注册组件
app.component('font-awesome-icon', FontAwesomeIcon)
```

### 3. 在组件中使用
```vue
<template>
  <!-- 基础使用 -->
  <font-awesome-icon :icon="['fas', 'user']" />
  
  <!-- 在按钮中使用 -->
  <el-button type="primary">
    <font-awesome-icon :icon="['fas', 'plus']" />
    添加
  </el-button>
  
  <!-- 设置大小和颜色 -->
  <font-awesome-icon 
    :icon="['fas', 'home']" 
    size="2x" 
    style="color: #409eff;" 
  />
</template>
```

## 📋 已配置的图标列表

| 图标名称 | 用途 | 示例 |
|---------|------|------|
| `user` | 用户相关 | `<font-awesome-icon :icon="['fas', 'user']" />` |
| `lock` | 安全/密码 | `<font-awesome-icon :icon="['fas', 'lock']" />` |
| `home` | 首页 | `<font-awesome-icon :icon="['fas', 'home']" />` |
| `cog` | 设置 | `<font-awesome-icon :icon="['fas', 'cog']" />` |
| `plus` | 添加 | `<font-awesome-icon :icon="['fas', 'plus']" />` |
| `minus` | 减少 | `<font-awesome-icon :icon="['fas', 'minus']" />` |
| `refresh` | 刷新 | `<font-awesome-icon :icon="['fas', 'refresh']" />` |
| `search` | 搜索 | `<font-awesome-icon :icon="['fas', 'search']" />` |
| `edit` | 编辑 | `<font-awesome-icon :icon="['fas', 'edit']" />` |
| `trash` | 删除 | `<font-awesome-icon :icon="['fas', 'trash']" />` |
| `save` | 保存 | `<font-awesome-icon :icon="['fas', 'save']" />` |
| `check` | 确认 | `<font-awesome-icon :icon="['fas', 'check']" />` |
| `times` | 关闭 | `<font-awesome-icon :icon="['fas', 'times']" />` |
| `eye` | 查看 | `<font-awesome-icon :icon="['fas', 'eye']" />` |
| `eye-slash` | 隐藏 | `<font-awesome-icon :icon="['fas', 'eye-slash']" />` |
| `download` | 下载 | `<font-awesome-icon :icon="['fas', 'download']" />` |
| `upload` | 上传 | `<font-awesome-icon :icon="['fas', 'upload']" />` |
| `arrow-left` | 左箭头 | `<font-awesome-icon :icon="['fas', 'arrow-left']" />` |
| `arrow-right` | 右箭头 | `<font-awesome-icon :icon="['fas', 'arrow-right']" />` |

## 🎯 测试页面

访问 `/icon-test` 路由可以查看所有图标的显示效果和测试状态。

## 📝 添加新图标

如果需要添加新的图标：

1. 从 `@fortawesome/free-solid-svg-icons` 导入图标
2. 添加到 `library.add()` 中
3. 在组件中使用

```typescript
// 1. 导入新图标
import { faNewIcon } from '@fortawesome/free-solid-svg-icons'

// 2. 添加到库
library.add(faNewIcon)

// 3. 使用
<font-awesome-icon :icon="['fas', 'new-icon']" />
```

## ⚠️ 注意事项

1. **图标名称转换**: 驼峰命名的图标在使用时需要转换为短横线命名
   - `faArrowLeft` → `arrow-left`
   - `faEyeSlash` → `eye-slash`

2. **按需导入**: 只导入需要的图标，避免打包体积过大

3. **图标前缀**: 目前配置的是 `fas` (Font Awesome Solid)，如需其他样式需要安装对应包

## 🔗 相关文档

- [Font Awesome Vue 官方文档](https://fontawesome.com/docs/web/use-with/vue/)
- [Font Awesome 图标库](https://fontawesome.com/icons)
- [Vue Font Awesome 组件 API](https://github.com/FortAwesome/vue-fontawesome)
