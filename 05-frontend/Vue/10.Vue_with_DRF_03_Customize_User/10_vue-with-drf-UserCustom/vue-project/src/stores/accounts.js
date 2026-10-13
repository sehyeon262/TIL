import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const API_URL = 'http://127.0.0.1:8000'
  // 공용으로 쓸 토큰 변수 정의
  const token = ref(null)

  const router = useRouter()

  const signUp = function (payload) {
    // 첫 번째 방법
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    const age = payload.age
    
    // 두 번째 방법 (구조 분해 할당)
    // const { username, password1, password2, age } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, 
        age,
      }
    })
      .then(res => {
        console.log('회원 가입이 완료되었습니다.')
        const password = password1
        logIn({ username, password })
      })
      .catch(err => console.log(err))
  }


  const logIn = function (payload) {
    // const username = payload.username
    // const password = payload.password
    const { username, password } = payload


    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then(res => {
        console.log('로그인이 완료되었습니다.')
        console.log(res.data)
        // 토큰 저장
        token.value = res.data.key
        router.push({ name: 'ArticleView' })
      })
      .catch(err => console.log(err))
  }


  const isLogin = computed(() => {
    return token.value ? true : false
  })


  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`
    })
      .then(res => {
        token.value = null  // 토큰 지우고
        router.push({ name: 'LogInView' })  // 로그인 페이지로 이동
      })
      .catch(err => console.log(err))
  }

  return {
    signUp,
    logIn,
    token,  // return에 없으면 저장 안 함!
    isLogin,
    logOut,
  }
}, { persist: true })