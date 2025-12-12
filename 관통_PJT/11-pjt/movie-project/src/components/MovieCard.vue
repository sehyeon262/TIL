<template>
  <div class="movie-card" @click="goToDetail">
    <img
      :src="posterUrl"
      :alt="movie.title"
      class="movie-poster"
    >
    <div class="movie-info">
      <h3 class="movie-title">{{ movie.title }}</h3>
      <p class="rating">평점: {{ movie.vote_average }}</p>
      <p class="release-date">{{ movie.release_date }}</p>
      <p class="movie-overview">{{ truncatedOverview }}</p>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  movie: {
    type: Object,
    required: true
  }
})

const router = useRouter()

const posterUrl = computed(() => {
  return props.movie.poster_path
    ? `https://image.tmdb.org/t/p/w500${props.movie.poster_path}`
    : 'https://via.placeholder.com/500x750?text=No+Image'
})

const truncatedOverview = computed(() => {
  const overview = props.movie.overview
  return overview.length > 100 ? overview.substring(0, 100) + '...' : overview
})

const goToDetail = () => {
  router.push(`/${props.movie.id}`)
}
</script>

<style scoped>
.movie-card {
  background-color: white;
  border: 1px solid #ddd;
  cursor: pointer;
}

.movie-card:hover {
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.movie-poster {
  width: 100%;
  height: 350px;
  object-fit: cover;
}

.movie-info {
  padding: 15px;
}

.movie-title {
  font-size: 1.1rem;
  margin-bottom: 8px;
  color: #333;
}

.rating {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 5px;
}

.release-date {
  font-size: 0.85rem;
  color: #999;
  margin-bottom: 10px;
}

.movie-overview {
  color: #666;
  font-size: 0.85rem;
  line-height: 1.4;
}
</style>
