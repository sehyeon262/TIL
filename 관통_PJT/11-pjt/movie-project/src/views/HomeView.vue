<template>
  <div class="home">
    <h1>영화 정보 사이트</h1>
    <p>TMDB API와 Youtube API를 활용한 영화 정보 제공 서비스</p>

    <div class="links">
      <RouterLink to="/movies" class="link-btn">최고 평점 영화 보기</RouterLink>
      <RouterLink to="/review-search" class="link-btn">리뷰 영상 검색</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.home {
  padding: 40px 20px;
  text-align: center;
}

h1 {
  font-size: 2rem;
  margin-bottom: 10px;
}

p {
  color: #666;
  margin-bottom: 40px;
}

.links {
  display: flex;
  gap: 20px;
  justify-content: center;
  flex-wrap: wrap;
}

.link-btn {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 3px;
}

.link-btn:hover {
  background-color: #0056b3;
}
</style>
