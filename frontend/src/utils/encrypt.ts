import JSEncrypt from 'jsencrypt'

// RSA公钥 (示例，实际使用时请替换为你的公钥)
const PUBLIC_KEY = `-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC...
-----END PUBLIC KEY-----`

// RSA私钥 (示例，实际使用时请替换为你的私钥)
const PRIVATE_KEY = `-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC...
-----END RSA PRIVATE KEY-----`

/**
 * RSA加密
 * @param text 要加密的文本
 * @returns 加密后的字符串
 */
export function rsaEncrypt(text: string): string {
  const encrypt = new JSEncrypt()
  encrypt.setPublicKey(PUBLIC_KEY)
  const encrypted = encrypt.encrypt(text)
  return encrypted || ''
}

/**
 * RSA解密
 * @param encryptedText 加密的文本
 * @returns 解密后的字符串
 */
export function rsaDecrypt(encryptedText: string): string {
  const decrypt = new JSEncrypt()
  decrypt.setPrivateKey(PRIVATE_KEY)
  const decrypted = decrypt.decrypt(encryptedText)
  return decrypted || ''
}

/**
 * Base64编码
 * @param text 要编码的文本
 * @returns 编码后的字符串
 */
export function base64Encode(text: string): string {
  return btoa(unescape(encodeURIComponent(text)))
}

/**
 * Base64解码
 * @param encodedText 编码的文本
 * @returns 解码后的字符串
 */
export function base64Decode(encodedText: string): string {
  return decodeURIComponent(escape(atob(encodedText)))
}
