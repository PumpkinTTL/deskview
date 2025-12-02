<template>
  <a-card title="PyWebView API 测试" :bordered="false">
    <a-space direction="vertical" size="large" style="width: 100%">
      <!-- 测试基础功能 -->
      <a-card size="small" title="基础功能测试" :bordered="false" style="background: #f5f5f5">
        <a-space direction="vertical" style="width: 100%">
          <a-input-group compact>
            <a-input v-model:value="testName" placeholder="输入你的名字" style="width: 200px" />
            <a-button type="primary" @click="testSayHello">
              <template #icon><font-awesome-icon :icon="['fas', 'user']" /></template>
              打招呼
            </a-button>
          </a-input-group>

          <a-button type="primary" @click="testGetSystemInfo">
            <template #icon><font-awesome-icon :icon="['fas', 'info-circle']" /></template>
            获取系统信息
          </a-button>

          <a-button type="primary" @click="testNotification">
            <template #icon><font-awesome-icon :icon="['fas', 'bell']" /></template>
            测试通知
          </a-button>
        </a-space>
      </a-card>

      <!-- 窗口控制 -->
      <a-card size="small" title="窗口控制" :bordered="false" style="background: #f5f5f5">
        <a-space>
          <a-button @click="resizeWindow(1280, 720)">标准尺寸</a-button>
          <a-button @click="resizeWindow(1920, 1080)">全高清</a-button>
          <a-button @click="resizeWindow(1024, 600)">最小尺寸</a-button>
        </a-space>
      </a-card>

      <!-- 执行命令 -->
      <a-card size="small" title="Shell 命令测试" :bordered="false" style="background: #f5f5f5">
        <a-space direction="vertical" style="width: 100%">
          <a-input-group compact>
            <a-input 
              v-model:value="shellCommand" 
              placeholder="输入 shell 命令（谨慎使用）" 
              style="width: 300px"
              @pressEnter="runCommand"
            />
            <a-button type="primary" danger @click="runCommand">
              <template #icon><font-awesome-icon :icon="['fas', 'terminal']" /></template>
              执行
            </a-button>
          </a-input-group>
          <a-alert message="⚠️ 此功能仅用于测试，生产环境请谨慎使用" type="warning" show-icon />
        </a-space>
      </a-card>

      <!-- 输出结果 -->
      <a-card size="small" title="API 调用结果" :bordered="false" style="background: #f0f0f0">
        <div v-if="apiResult" class="result-box">
          <pre>{{ JSON.stringify(apiResult, null, 2) }}</pre>
        </div>
        <a-empty v-else description="暂无调用结果" />
      </a-card>
    </a-space>
  </a-card>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { message } from 'ant-design-vue'

const testName = ref('用户')
const shellCommand = ref('echo Hello from PyWebView!')
const apiResult = ref<any>(null)

// 检查 pywebview API 是否可用
const checkPyWebViewAPI = () => {
  if (!window.pywebview || !window.pywebview.api) {
    message.error('PyWebView API 不可用，请在桌面应用中运行')
    return false
  }
  return true
}

// 测试打招呼
const testSayHello = async () => {
  if (!checkPyWebViewAPI()) return
  
  try {
    const result = await window.pywebview.api.say_hello(testName.value)
    apiResult.value = result
    if (result.success) {
      message.success(result.message)
    }
  } catch (error) {
    message.error(`调用失败: ${error}`)
    console.error(error)
  }
}

// 测试获取系统信息
const testGetSystemInfo = async () => {
  if (!checkPyWebViewAPI()) return
  
  try {
    const result = await window.pywebview.api.get_system_info()
    apiResult.value = result
    if (result.success) {
      message.success('系统信息获取成功')
    }
  } catch (error) {
    message.error(`调用失败: ${error}`)
    console.error(error)
  }
}

// 测试通知
const testNotification = async () => {
  if (!checkPyWebViewAPI()) return
  
  try {
    const result = await window.pywebview.api.test_notification(
      '测试通知',
      '这是一条来自前端的测试通知'
    )
    apiResult.value = result
    if (result.success) {
      message.success('通知已发送到后端')
    }
  } catch (error) {
    message.error(`调用失败: ${error}`)
    console.error(error)
  }
}

// 调整窗口大小
const resizeWindow = async (width: number, height: number) => {
  if (!checkPyWebViewAPI()) return
  
  try {
    const result = await window.pywebview.api.resize_window(width, height)
    apiResult.value = result
    if (result.success) {
      message.success(result.message)
    }
  } catch (error) {
    message.error(`调用失败: ${error}`)
    console.error(error)
  }
}

// 执行 shell 命令
const runCommand = async () => {
  if (!checkPyWebViewAPI()) return
  if (!shellCommand.value.trim()) {
    message.warning('请输入命令')
    return
  }
  
  try {
    const result = await window.pywebview.api.run_shell_command(shellCommand.value)
    apiResult.value = result
    if (result.success) {
      message.success('命令执行成功')
    } else {
      message.error('命令执行失败')
    }
  } catch (error) {
    message.error(`调用失败: ${error}`)
    console.error(error)
  }
}
</script>

<style scoped lang="less">
.result-box {
  background: #fff;
  border: 1px solid #d9d9d9;
  border-radius: 4px;
  padding: 12px;
  max-height: 400px;
  overflow: auto;
  
  pre {
    margin: 0;
    font-family: 'Courier New', monospace;
    font-size: 12px;
    line-height: 1.6;
    color: #333;
  }
}
</style>
