import { createRouter, createWebHistory } from 'vue-router'
import BabosoView from '@/views/BabosoView.vue'
const routes = [
  {
    path: '/',
    name: 'Baboso',
    component: BabosoView

  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
