<template>
  <div class="q-pa-md">
    <form class="register" @submit.prevent="register">
      <h4>Register to post memories</h4>
      <p class="text-weight-bold">Required</p>
      <div class="row q-pa-xs">
        <label class="q-pr-sm">Email</label>
        <input required v-model="email" id="email" type="text" placeholder="your@email.com" autocapitalize="none"/>
      </div>
      <div class="row q-pa-xs">
        <label class="q-pr-sm">Password</label>
        <input required v-model="password" id="password" type="password"/>
      </div>
      <div class="row q-pa-xs">
        <label class="q-pr-sm">Password (again)</label>
        <input required v-model="password_again" id="password_again" type="password"/>
        <div class="text-negative q-ml-sm" v-if="show_password_error">Passwords must match</div>
      </div>
      <hr />
      <p class="text-weight-bold">Optional - So people know who posted your memories!</p>
      <div class="row q-pa-xs">
        <label class="q-pr-sm">First Name</label>
        <input v-model="first_name" id="first_name" type="text"/>
      </div>
      <div class="row q-pa-xs">
        <label class="q-pr-sm">Last Name</label>
        <input v-model="last_name" id="last_name" type="text"/>
      </div>
      <hr/>
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script lang="ts">
import axios from 'axios';
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class Login extends Vue{
  private email = ''
  private password = ''
  private password_again = ''
  private first_name = ''
  private last_name = ''
  private show_password_error = false
  public register(): void {
    const { email, password, password_again, first_name, last_name } = this
    if (password != password_again) {
      this.show_password_error = true
      return
    } else {
      this.show_password_error = false
    }
    axios({url: `${ process.env.API_URL }api/register/`, data: {email, password, first_name, last_name}, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
      .then(() => {
        this.$store.dispatch('authModule/authRequest', { username: email, password })
          .then(() => this.$router.push('/'))
          .catch((err) => console.log(err))
      })
      .catch(e => {
        console.error('Error registering user:', e)
      })
  }
}
</script>
