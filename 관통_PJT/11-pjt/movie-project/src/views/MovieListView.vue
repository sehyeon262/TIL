<template>
  <div class="movie-list">
    <h1>최고 평점 영화</h1>

    <div v-if="loading" class="loading">
      <p>영화 정보를 불러오는 중...</p>
    </div>

    <div v-else-if="error" class="error">
      <p>{{ error }}</p>
    </div>

    <div v-else class="movies-grid">
      <MovieCard
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import MovieCard from '../components/MovieCard.vue'

const movies = ref([])
const loading = ref(true)
const error = ref(null)

const fetchTopRatedMovies = async () => {
  try {
    loading.value = true
    const apiKey = import.meta.env.VITE_TMDB_API_KEY

    const response = await axios.get('https://api.themoviedb.org/3/movie/top_rated', {
      headers: {
        Authorization: `Bearer ${apiKey}`
      },
      params: {
        language: 'ko-KR',
        page: 1
      }
    })

    movies.value = response.data.results
  } catch (err) {
    console.error('영화 데이터를 불러오는 중 오류 발생:', err)
    error.value = '영화 정보를 불러오는데 실패했습니다.'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchTopRatedMovies()
})
</script>

<style scoped>
.movie-list {
  padding: 20px 0;
}

h1 {
  font-size: 1.8rem;
  margin-bottom: 20px;
}

.loading,
.error {
  text-align: center;
  padding: 40px 0;
}

.error {
  color: red;
}

.movies-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 20px;
}
</style>
