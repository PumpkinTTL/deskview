/**
 * PyWebView API 工具函数
 * 用于封装与 Python 后端的交互
 */

/**
 * 检查是否在 PyWebView 环境中
 */
export function isPyWebViewEnvironment(): boolean {
  return !!(window.pywebview && window.pywebview.api)
}

/**
 * 调整窗口大小
 * @param width 窗口宽度
 * @param height 窗口高度
 * @returns Promise<{success: boolean, message: string}>
 */
export async function resizeWindow(width: number, height: number): Promise<{success: boolean, message: string}> {
  if (!isPyWebViewEnvironment()) {
    return {
      success: false,
      message: '当前不在 PyWebView 环境中'
    }
  }

  try {
    const result = await window.pywebview!.api.resize_window(width, height)
    return result
  } catch (error) {
    console.error('调整窗口大小失败:', error)
    return {
      success: false,
      message: `调整窗口大小失败: ${error}`
    }
  }
}

/**
 * 测试 API 连接
 * @param name 测试名称
 * @returns Promise<string>
 */
export async function testApiConnection(name: string = 'Frontend'): Promise<string> {
  if (!isPyWebViewEnvironment()) {
    return 'Mock: API 连接测试 - 当前不在 PyWebView 环境中'
  }

  try {
    const result = await window.pywebview!.api.say_hello(name)
    return result
  } catch (error) {
    console.error('API 连接测试失败:', error)
    return `API 连接测试失败: ${error}`
  }
}

/**
 * 获取窗口信息
 * @returns Promise<{success: boolean, title?: string, resizable?: boolean, message?: string}>
 */
export async function getWindowInfo(): Promise<{success: boolean, title?: string, resizable?: boolean, message?: string}> {
  if (!isPyWebViewEnvironment()) {
    return {
      success: false,
      message: '当前不在 PyWebView 环境中'
    }
  }

  try {
    const result = await window.pywebview!.api.get_window_info()
    return result
  } catch (error) {
    console.error('获取窗口信息失败:', error)
    return {
      success: false,
      message: `获取窗口信息失败: ${error}`
    }
  }
}

/**
 * 窗口大小预设
 */
export const WindowSizes = {
  LOGIN: { width: 800, height: 600 },
  MAIN: { width: 1200, height: 800 },
  COMPACT: { width: 1000, height: 700 },
  FULLSCREEN: { width: 1400, height: 900 }
} as const

/**
 * 应用窗口大小预设
 * @param preset 预设名称
 * @returns Promise<{success: boolean, message: string}>
 */
export async function applyWindowSizePreset(preset: keyof typeof WindowSizes): Promise<{success: boolean, message: string}> {
  const size = WindowSizes[preset]
  return await resizeWindow(size.width, size.height)
}
