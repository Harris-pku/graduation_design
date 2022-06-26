// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

/* eslint-disable */

import Vue from 'vue'
import App from './App.vue'
import Index from './views/index.vue'
import Search from "./views/Search.vue"
import About from "./views/About.vue"
import Help from "./views/Help.vue"
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import router from './router'
import axios from 'axios'
import { Message } from 'element-ui'
// import ECharts from 'vue-echarts'
// import 'echarts'

Vue.use(ElementUI).use(router)
Vue.prototype.$axios = axios
Vue.prototype.$url = 'http://127.0.0.1:8000'
Vue.prototype.$message = Message

// Vue.config.productionTip = false

/* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   router,
//   components: { App },
//   template: '<App/>'
// })



new Vue({
    el: '#app',
    // render: h => h(App),
    render: h => h(App),
    router
});
