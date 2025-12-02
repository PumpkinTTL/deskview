import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/Home.vue'),
    meta: {
      title: '桌面端模板',
      width: 1280,
      height: 720,
    },
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// 路由守卫
router.beforeEach(async (to, _from, next) => {
  // 1. 设置页面标题
  if (to.meta?.title) {
    document.title = `${to.meta.title} - 桌面助手`
  }

  // 2. 调整窗口大小（仅在 WebView 环境下且有尺寸配置时）
  const meta = to.meta as any
  if (meta?.width && meta?.height && window.pywebview?.api?.resize_window) {
    try {
      const result = await window.pywebview.api.resize_window(meta.width, meta.height)
      if (result.success) {
        console.log(`路由切换: ${result.message}`)
      } else {
        console.warn(`窗口调整失败: ${result.message}`)
      }
    } catch (error) {
      console.error('调整窗口大小失败:', error)
    }
  }

  next()
})

export default router
