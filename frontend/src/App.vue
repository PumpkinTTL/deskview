<template>
  <div id="app">
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component"/>
      </transition>
    </router-view>
  </div>
</template>

<script setup lang="ts">
import {ref} from 'vue'

function sayHello() {
  pywebview.api.say_hello('弟弟')
}

// 这里可以添加全局逻辑
const title = ref('标题')
</script>

<style lang="less">
#app {
  min-height: 100vh;
}

.app-header {
  background-color: @bg-color;
  border-bottom: 1px solid @border-base;
  padding: 0;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 @spacing-lg;

  h1 {
    margin: 0;
    color: @primary-color;
  }
}

.header-menu {
  border-bottom: none;
}

.app-main {
  padding: 0;
  background-color: @bg-color-page;
}

// 页面切换动画
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
