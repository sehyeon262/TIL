<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div id="app">
    <nav class="navbar">
      <div class="container">
        <RouterLink to="/">영화정보</RouterLink>
        <RouterLink to="/movies">최고평점</RouterLink>
        <RouterLink to="/review-search">리뷰검색</RouterLink>
      </div>
    </nav>
    <div class="container">
      <RouterView />
    </div>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
  color: #333;
}

#app {
  min-height: 100vh;
}

.navbar {
  background-color: #fff;
  border-bottom: 1px solid #ddd;
  padding: 15px 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.navbar .container {
  display: flex;
  gap: 30px;
}

.navbar a {
  color: #333;
  text-decoration: none;
  padding: 5px 10px;
}

.navbar a:hover,
.navbar a.router-link-active {
  background-color: #007bff;
  color: white;
  border-radius: 3px;
}
</style>
