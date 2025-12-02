// 主题切换工具

export type ThemeMode = 'light' | 'dark' | 'auto'

const THEME_KEY = 'app-theme'

/**
 * 获取当前主题模式
 */
export function getCurrentTheme(): ThemeMode {
  const saved = localStorage.getItem(THEME_KEY) as ThemeMode
  return saved || 'auto'
}

/**
 * 设置主题模式
 * @param theme 主题模式：light | dark | auto
 */
export function setTheme(theme: ThemeMode) {
  localStorage.setItem(THEME_KEY, theme)
  applyTheme(theme)
}

/**
 * 应用主题
 * @param theme 主题模式
 */
export function applyTheme(theme: ThemeMode) {
  const html = document.documentElement

  // 移除之前的主题类
  html.removeAttribute('data-theme')
  html.classList.remove('light', 'dark')

  if (theme === 'auto') {
    // 自动模式：根据系统设置，不设置 data-theme 让 CSS 媒体查询处理
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
    if (prefersDark) {
      html.classList.add('dark')
    } else {
      html.classList.add('light')
    }
  } else {
    // 手动设置模式
    html.setAttribute('data-theme', theme)
    html.classList.add(theme)
  }
}

/**
 * 切换主题（在 light 和 dark 之间切换）
 */
export function toggleTheme() {
  const current = getCurrentTheme()
  const newTheme: ThemeMode = current === 'dark' ? 'light' : 'dark'
  setTheme(newTheme)
  return newTheme
}

/**
 * 监听系统主题变化
 */
export function watchSystemTheme() {
  const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)')
  
  const handleChange = () => {
    const currentTheme = getCurrentTheme()
    if (currentTheme === 'auto') {
      applyTheme('auto')
    }
  }
  
  mediaQuery.addEventListener('change', handleChange)
  
  // 返回清理函数
  return () => {
    mediaQuery.removeEventListener('change', handleChange)
  }
}

/**
 * 初始化主题
 */
export function initTheme() {
  const theme = getCurrentTheme()
  applyTheme(theme)
  
  // 监听系统主题变化
  return watchSystemTheme()
}

/**
 * 获取当前是否为暗色模式
 */
export function isDarkMode(): boolean {
  return document.documentElement.getAttribute('data-theme') === 'dark'
}

/**
 * 获取系统是否偏好暗色模式
 */
export function isSystemDarkMode(): boolean {
  return window.matchMedia('(prefers-color-scheme: dark)').matches
}
