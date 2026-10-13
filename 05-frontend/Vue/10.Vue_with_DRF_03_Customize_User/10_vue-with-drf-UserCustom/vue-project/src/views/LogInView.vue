<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="logIn">
      <label for="username">username: </label><br>
      <input type="text" id="username" v-model.trim="username">
      <br>
      <label for="password">password: </label><br>
      <input type="password" id="password" v-model.trim="password">
      <br>
      <input type="submit" value="LogIn">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/accounts'

  const accountStore = useAccountStore()

  const username = ref(null)
  const password = ref(null)

  const logIn = function () {
    // 사용자의 입력값을 객체(payload)로 만들고
    const payload = {
      username: username.value,
      password: password.value,
    }
    // 객체를 logIn으로 전달
    accountStore.logIn(payload)
  }
  
</script>

<style>

</style>
