<template>
  <div class="home-layout">
    <a-layout style="min-height: 100vh">
      <a-layout-sider
        v-model:collapsed="collapsed"
        :trigger="null"
        collapsible
        :style="{ background: '#fff' }"
        :width="220"
      >
        <div class="logo">
          <font-awesome-icon :icon="['fas', 'code']" class="logo-icon" />
          <span v-if="!collapsed">桌面应用模板</span>
        </div>
        <a-menu
          v-model:selectedKeys="selectedKeys"
          mode="inline"
          @select="handleMenuSelect"
          :style="{ borderRight: 0 }"
        >
          <a-menu-item key="dashboard">
            <template #icon>
              <font-awesome-icon :icon="['fas', 'home']" />
            </template>
            <span>仪表盘</span>
          </a-menu-item>
          <a-menu-item key="api-test">
            <template #icon>
              <font-awesome-icon :icon="['fas', 'flask']" />
            </template>
            <span>API测试</span>
          </a-menu-item>
          <a-menu-item key="about">
            <template #icon>
              <font-awesome-icon :icon="['fas', 'info-circle']" />
            </template>
            <span>关于模板</span>
          </a-menu-item>
        </a-menu>

        <div class="sider-trigger" @click="collapsed = !collapsed">
          <font-awesome-icon :icon="collapsed ? ['fas', 'angles-right'] : ['fas', 'angles-left']" />
        </div>
      </a-layout-sider>

      <a-layout>
        <a-layout-header class="header">
          <a-space>
            <a-button
              type="text"
              @click="collapsed = !collapsed"
              class="trigger-btn"
            >
              <font-awesome-icon :icon="collapsed ? ['fas', 'angles-right'] : ['fas', 'angles-left']" />
            </a-button>
            <h2>{{ currentTitle }}</h2>
          </a-space>
        </a-layout-header>

        <a-layout-content class="content">
          <template v-if="selectedKeys[0] === 'dashboard'">
            <a-card :title="currentTitle" :bordered="false">
              <p>这里是桌面端应用的主界面示例，你可以在此基础上快速搭建自己的业务页面。</p>
              <a-space>
                <a-button type="primary" @click="handleQuickAction">测试请求提示</a-button>
                <a-button>普通按钮</a-button>
              </a-space>
            </a-card>
          </template>
          
          <template v-else-if="selectedKeys[0] === 'api-test'">
            <ApiTest />
          </template>
          
          <template v-else>
            <a-card :title="currentTitle" :bordered="false">
              <p>这是一个基于 Vue 3 + Ant Design Vue 的桌面端模板项目。</p>
              <p>你可以：</p>
              <ul>
                <li>集成到 PyWebView / Electron 等桌面容器中</li>
                <li>使用 Pinia 管理全局状态</li>
                <li>按需新增路由和页面组件</li>
              </ul>
            </a-card>
          </template>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { message } from 'ant-design-vue'
import ApiTest from '@/components/ApiTest.vue'

const collapsed = ref(false)
const selectedKeys = ref<string[]>(['dashboard'])

const currentTitle = computed(() => {
  const titles: Record<string, string> = {
    dashboard: '桌面应用首页',
    'api-test': 'PyWebView API 测试',
    about: '关于本模板',
  }
  return titles[selectedKeys.value[0]] || '桌面应用模板'
})

const handleMenuSelect = ({ key }: { key: string }) => {
  selectedKeys.value = [key]
}

const handleQuickAction = () => {
  message.success('Ant Design Vue 模板工作正常')
}
</script>

<style scoped lang="less">
.home-layout {
  width: 100%;
  height: 100vh;
}

.logo {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  color: #1890ff;
  font-size: 16px;
  font-weight: bold;
  border-bottom: 1px solid #f0f0f0;
  padding: 0 16px;

  .logo-icon {
    font-size: 24px;
  }
}

.sider-trigger {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border-top: 1px solid #f0f0f0;
  color: #666;
  transition: all 0.3s;

  &:hover {
    background: #f5f5f5;
    color: #1890ff;
  }
}

.header {
  background: #fff;
  padding: 0 24px;
  border-bottom: 1px solid #f0f0f0;
  display: flex;
  align-items: center;

  h2 {
    margin: 0;
    color: #333;
    font-size: 18px;
  }

  .trigger-btn {
    font-size: 18px;
    color: #666;

    &:hover {
      color: #1890ff;
    }
  }
}

.content {
  margin: 24px 16px;
  padding: 24px;
  background: #fff;
  min-height: 280px;
}

:deep(.ant-layout-sider) {
  position: relative;
}

// 深色模式适配
@media (prefers-color-scheme: dark) {
  .home-layout {
    :deep(.ant-layout) {
      background: #141414;
    }

    :deep(.ant-layout-sider) {
      background: #1f1f1f !important;
      border-right: 1px solid #303030;
    }

    .logo {
      color: #1890ff;
      border-bottom: 1px solid #303030;
    }

    .sider-trigger {
      border-top: 1px solid #303030;
      color: rgba(255, 255, 255, 0.65);

      &:hover {
        background: #111;
        color: #1890ff;
      }
    }

    :deep(.ant-menu) {
      background: #1f1f1f;
      color: #fff;
    }

    :deep(.ant-menu-item) {
      color: rgba(255, 255, 255, 0.85);

      &:hover {
        color: #1890ff;
      }

      &.ant-menu-item-selected {
        background: #111;
        color: #1890ff;
      }
    }

    .header {
      background: #1f1f1f;
      border-bottom: 1px solid #303030;

      h2 {
        color: #fff;
      }

      .trigger-btn {
        color: rgba(255, 255, 255, 0.65);

        &:hover {
          color: #1890ff;
        }
      }
    }

    .content {
      background: #141414;
    }
  }
}
</style>
