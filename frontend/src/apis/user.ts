import request from '@/utils/request'

// 用户相关API接口
export interface User {
  id: number
  username: string
  email: string
  avatar?: string
}

export interface LoginParams {
  username: string
  password: string
}

export interface LoginResponse {
  token: string
  user: User
}

/**
 * 用户登录
 */
export function login(data: LoginParams) {
  return request<LoginResponse>({
    url: '/auth/login',
    method: 'post',
    data
  })
}

/**
 * 获取用户信息
 */
export function getUserInfo() {
  return request<User>({
    url: '/user/info',
    method: 'get'
  })
}

/**
 * 更新用户信息
 */
export function updateUser(data: Partial<User>) {
  return request<User>({
    url: '/user/update',
    method: 'put',
    data
  })
}
