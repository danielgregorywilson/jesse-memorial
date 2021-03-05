<template>
  <div class="q-pa-md">
    <form class="login" @submit.prevent="login">
      <h4>Log in to post memories</h4>
      <div class="row q-pa-xs">
        <label class="q-pr-sm">Email</label>
        <input required v-model="username" id="username" type="email" placeholder="your@email.com" autocapitalize="none"/>
      </div>
      <div class="row q-pa-xs">
        <label class="q-pr-sm">Password</label>
        <input required v-model="password" id="password" type="password"/>
      </div>
      <hr/>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class Login extends Vue{
  private username = ''
  private password = ''
  public login(): void {
    const { username, password } = this
    this.$store.dispatch('authModule/authRequest', { username, password })
      .then(() => this.$router.push('/'))
      .catch((err) => console.log(err))
  }
}
</script>
