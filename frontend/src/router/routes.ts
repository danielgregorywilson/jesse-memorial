import { Route, RouteConfig } from 'vue-router';

import authState from '../store/modules/auth/state'
import userState from '../store/modules/user/state'

type Next = (path?: string) => void

const ifNotAuthenticated = (to: Route, from: Route, next: Next) => {
  if (!authState.token) { // TODO: This should use the isAuthenticated getter
    next()
    return
  }
  next('/')
}

const ifAuthenticated = (to: Route, from: Route, next: Next) => {
  if (!!authState.token) { // TODO: This should use the isAuthenticated getter
    next()
    return
  }
  next('auth/login')
}

const ifManager = (to: Route, from: Route, next: Next) => {
  if (userState.profile.is_manager) {
    next()
    return
  }
  next('dashboard')
}

const ifCanViewReview = (to: Route, from: Route, next: Next) => {
  if (userState.profile.prs_can_view.indexOf(parseInt(to.params.pk)) != -1) {
    next()
    return
  } else {
    console.info('User can not view PR', to.params.pk, 'Redirecting to dashboard.')
    next('dashboard')
  }
}

const ifCanViewNote = (to: Route, from: Route, next: Next) => {
  if (userState.profile.notes_can_view.indexOf(parseInt(to.params.pk)) != -1) {
    next()
    return
  } else {
    next('dashboard')
  }
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
        beforeEnter: ifNotAuthenticated,
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
