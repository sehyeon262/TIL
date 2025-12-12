<template>
  <div class="movie-detail">
    <div v-if="loading" class="loading">
      <p>영화 정보를 불러오는 중...</p>
    </div>

    <div v-else-if="error" class="error">
      <p>{{ error }}</p>
      <button @click="$router.push('/movies')" class="back-btn">목록으로 돌아가기</button>
    </div>

    <div v-else-if="movie">
      <MovieDetailInfo :movie="movie" @show-trailer="showTrailerModal = true" />

      <YoutubeTrailerModal
        :is-open="showTrailerModal"
        :movie-title="movie.title"
        :title="`${movie.title} 공식 예고편`"
        @close="showTrailerModal = false"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import MovieDetailInfo from '../components/MovieDetailInfo.vue'
import YoutubeTrailerModal from '../components/YoutubeTrailerModal.vue'

const route = useRoute()
const router = useRouter()

const movie = ref(null)
const loading = ref(true)
const error = ref(null)
const showTrailerModal = ref(false)

const fetchMovieDetail = async () => {
  try {
    loading.value = true
    const apiKey = import.meta.env.VITE_TMDB_API_KEY
    const movieId = route.params.movieId

    const response = await axios.get(`https://api.themoviedb.org/3/movie/${movieId}`, {
      headers: {
        Authorization: `Bearer ${apiKey}`
      },
      params: {
        language: 'ko-KR'
      }
    })

    movie.value = response.data
  } catch (err) {
    console.error('영화 상세 정보를 불러오는 중 오류 발생:', err)
    error.value = '영화 정보를 불러오는데 실패했습니다.'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchMovieDetail()
})
</script>

<style scoped>
.movie-detail {
  padding: 20px 0;
}

.loading,
.error {
  text-align: center;
  padding: 40px 0;
}

.error {
  color: red;
}

.back-btn {
  margin-top: 15px;
  padding: 10px 20px;
  background-color: #6c757d;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.back-btn:hover {
  background-color: #5a6268;
}
</style>
