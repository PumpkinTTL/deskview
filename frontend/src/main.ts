import {createApp} from 'vue'
import {createPinia} from 'pinia'
import router from '@/router'
import App from './App.vue'

// 样式导入
import 'animate.css'
import '@/style.css'

// Font Awesome 图标
import {library} from '@fortawesome/fontawesome-svg-core'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

import {
    // 已有的图标
    faUser,
    faLock,
    faEye,
    faEyeSlash,
    faSignInAlt,
    faSpinner,
    faInfoCircle,
    faBriefcase,
    faCode,
    faTerminal,
    faWindowMaximize,
    faRefresh,
    faHome,
    faAnglesLeft,
    faAnglesRight,
    faPlus,
    faTrash,
    faSync,
    faEdit,
    faRightLeft,
    faCopy,
    faFlask,
    faBell
} from '@fortawesome/free-solid-svg-icons'
import {
    faWeixin,
    faQq,
    faMicrosoft
} from '@fortawesome/free-brands-svg-icons'
// 添加品牌图标需要单独引入


// 添加图标到库
library.add(
    faUser, faLock, faEye, faEyeSlash, faSignInAlt, faSpinner,
    faInfoCircle, faBriefcase, faWeixin, faQq, faMicrosoft,
    faCode, faTerminal, faWindowMaximize, faRefresh, faHome,
    faAnglesLeft, faAnglesRight, faPlus, faTrash, faSync, faEdit, 
    faRightLeft, faCopy, faFlask, faBell
)

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router)
app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')
