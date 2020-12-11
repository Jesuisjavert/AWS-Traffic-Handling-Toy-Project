import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: () => import('@/components/core/Index.vue'),
      children: [
        {
          path: '',
          name: 'Home',
          component: () => import('@/views/home/Index.vue'),
        },
        {
          path: '/about',
          name: 'About me',
          component: () => import('@/views/about/Index.vue'),
        },
        {
          path: '/analysis',
          name: 'Analysis',
          component: () => import('@/views/analysis/Index.vue'),
        },
        {
          path: '/membership',
          name: 'Membership',
          component: () => import('@/views/membership/Index.vue'),
          meta: { src: require('@/assets/javert1.jpg') },
        },
      ],
    },
  ],
})
