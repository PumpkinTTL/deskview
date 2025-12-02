/// <reference types="vite/client" />

// PyWebView API 类型声明
interface PyWebViewAPI {
  resize_window(width: number, height: number): Promise<{success: boolean, message: string}>
  say_hello(name: string): Promise<string>
  get_window_info(): Promise<{success: boolean, title?: string, resizable?: boolean, message?: string}>
}

interface PyWebView {
  api: PyWebViewAPI
}

declare global {
  interface Window {
    pywebview?: PyWebView
  }
}
