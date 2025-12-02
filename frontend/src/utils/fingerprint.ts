import FingerprintJS from '@fingerprintjs/fingerprintjs'

/**
 * 获取浏览器指纹
 * @returns Promise<string> 返回唯一的浏览器指纹ID
 */
export async function getBrowserFingerprint(): Promise<string> {
  try {
    // 初始化FingerprintJS
    const fp = await FingerprintJS.load()
    
    // 获取指纹
    const result = await fp.get()
    
    return result.visitorId
  } catch (error) {
    console.error('获取浏览器指纹失败:', error)
    return ''
  }
}

/**
 * 获取详细的浏览器信息
 * @returns Promise<object> 返回详细的浏览器信息
 */
export async function getBrowserInfo(): Promise<any> {
  try {
    const fp = await FingerprintJS.load()
    const result = await fp.get()
    
    return {
      visitorId: result.visitorId,
      confidence: result.confidence,
      components: result.components
    }
  } catch (error) {
    console.error('获取浏览器信息失败:', error)
    return null
  }
}
