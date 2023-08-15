import { createRouter, createWebHistory } from 'vue-router'
import Function1IndexView from '../views/function1/Function1IndexView'
import Function2IndexView from '../views/function2/Function2IndexView'
import Function3IndexView from '../views/function3/Function3IndexView'
import UserBotIndexView from '../views/user/bot/UserBotIndexView'
import NotFound from '../views/error/NotFound'



const routes = [
  {
    path: "/",
    name: "home",
    redirect: "/function1/"
  },
  {
    path: "/function1/",
    name: "function1_index",
    component: Function1IndexView,
  },
  {
    path: "/function2/",
    name: "function2_index",
    component: Function2IndexView,
  },
  {
    path: "/function3/",
    name: "function3_index",
    component: Function3IndexView,
  },
  {
    path: "/user/bot/",
    name: "user_bot_index",
    component: UserBotIndexView,
  },
  {
    path: "/404/",
    name: "404",
    component: NotFound,
  },
  {
    path: "/:catchAll(.*)",
    redirect: "/404/"
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
