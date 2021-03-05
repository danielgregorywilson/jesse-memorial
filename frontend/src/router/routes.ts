import { Route, RouteConfig } from 'vue-router';

import authState from '../store/modules/auth/state'

type Next = (path?: string) => void

const ifAuthenticated = (to: Route, from: Route, next: Next) => {
  if (!!authState.token) { // TODO: This should use the isAuthenticated getter
    next()
    return
  }
  next('auth/login')
}

// TODO: Add a reset password view as in Django version, unless we're authenticating with LDAP
const routes: RouteConfig[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/', redirect: '/dashboard' },
      {
        path: '/dashboard',
        name: 'dashboard',
        component: () => import('pages/Dashboard.vue'),
      },
      {
        path: '/upload',
        name: 'upload',
        component: () => import('pages/Upload.vue'),
        beforeEnter: ifAuthenticated,
      },
    ]
  },
  {
    path: '/auth',
    component: () => import('layouts/AuthLayout.vue'),
    children: [
      {
        path: 'login',
        name: 'login',
        component: () => import('pages/auth/Login.vue'),
      },
      {
        path: 'register',
        name: 'register',
        component: () => import('pages/auth/Register.vue'),
      },
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
];

export default routes;
