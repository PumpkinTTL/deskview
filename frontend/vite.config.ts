import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { AntDesignVueResolver } from 'unplugin-vue-components/resolvers'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    AutoImport({
      resolvers: [
        AntDesignVueResolver(),
      ],
      imports: [
        'vue',
        'vue-router',
        'pinia',
      ],
      dts: true,
    }),
    Components({
      resolvers: [
        // 配置 Ant Design Vue 自动导入
        AntDesignVueResolver({
          importStyle: false, // css in js
        }),
      ],
    }),
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  css: {
    preprocessorOptions: {
      less: {
        // 自动导入全局样式文件
        additionalData: `@import "@/styles/variables.less";`,
        javascriptEnabled: true,
      },
    },
  },
  server: {
    port: 9696,
  },
})
