import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Index from "../views/Index.vue"
import Search from "../views/Search.vue"
import About from "../views/About.vue"
import Help from "../views/Help.vue"
import ElementUI from 'element-ui'

Vue.use(Router).use(ElementUI)

const contextInfo = require.context('../views', false, /.vue$/);
let routerAry = []
contextInfo.keys().forEach(fileName => {
    const pathConfig = contextInfo(fileName)
    let path = "/" + fileName.substring(2,fileName.length-4)
    routerAry.push({
        path,
        component: pathConfig.default
    })
})

const routerList = [
    {
        path: "/",
        redirect: "/home",
    },
    {
        path: "/home",
        component: Index
    },{
        path: "/search",
        component: Search
    },{
        path: '/about',
        component: About
    },{
        path: "/help",
        component: Help
    },
]
const newRouterAry = routerList.concat(routerAry)
const router = new Router({
    routes: newRouterAry
})

export default router

// export default new Router({
//   // routes: [
//   //   {
//   //     path: '/',
//   //     name: 'HelloWorld',
//   //     component: HelloWorld
//   //   }
//   // ]
//   routes: [
//     // {
//     //   path: '/',
//     //   redirect: '/home'
//     // },
//     {
//       path: '/home',
//       component: () => import('../views/Index'),
//       // meta: {title: '主页'}
//     },
//     {
//       path: '/search',
//       component: () => import('../views/Index'),
//       meta: {title: '搜索界面'}
//     },
//     {
//       path: '/about',
//       component: About, /*() => import('../components/Index.vue'),*/
//       meta: {title: '关于'}
//     },
//     {
//       path: '/help',
//       component: Help, /*() => import('../components/Index.vue'),*/
//       meta: {title: '帮助'}
//     }
//   ]
// })


// 查询指定文件夹下的vue页面，自动注册路由
// 仅适用于：一个文件夹下的多个路由页面。用于简单的页面的注册
// pathConfig.default的内容，是指定的vue页面的default模块内容，等同于: () => import('xxxx')

