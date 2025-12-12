<template>
  <div class="movie-detail-info">
    <div class="movie-poster">
      <img :src="posterUrl" :alt="movie.title">
    </div>
    <div class="movie-details">
      <h1>{{ movie.title }}</h1>
      <p class="rating">평점: {{ movie.vote_average }}/10</p>
      <p class="vote-count">투표 수: {{ movie.vote_count }}</p>
      <p class="release-date">개봉일: {{ movie.release_date }}</p>
      <div class="genres">
        <span v-for="genre in movie.genres" :key="genre.id" class="genre-tag">
          {{ genre.name }}
        </span>
      </div>
      <div class="overview">
        <h3>줄거리</h3>
        <p>{{ movie.overview || '줄거리 정보가 없습니다.' }}</p>
      </div>
      <button @click="$emit('show-trailer')" class="trailer-btn">
        공식 예고편
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  movie: {
    type: Object,
    required: true
  }
})

defineEmits(['show-trailer'])

const posterUrl = computed(() => {
  return props.movie.poster_path
    ? `https://image.tmdb.org/t/p/w500${props.movie.poster_path}`
    : 'https://via.placeholder.com/500x750?text=No+Image'
})
</script>

<style scoped>
.movie-detail-info {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 30px;
  margin-bottom: 30px;
  background-color: white;
  padding: 20px;
  border: 1px solid #ddd;
}

.movie-poster img {
  width: 100%;
}

.movie-details h1 {
  font-size: 1.8rem;
  margin-bottom: 15px;
}

.movie-details p {
  margin-bottom: 8px;
  color: #666;
}

.rating {
  font-weight: bold;
}

.genres {
  display: flex;
  gap: 8px;
  margin: 15px 0;
  flex-wrap: wrap;
}

.genre-tag {
  background-color: #f0f0f0;
  padding: 5px 12px;
  border-radius: 15px;
  font-size: 0.9rem;
  color: #666;
}

.overview h3 {
  font-size: 1.2rem;
  margin-bottom: 10px;
  margin-top: 15px;
}

.overview p {
  line-height: 1.6;
  color: #333;
}

.trailer-btn {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.trailer-btn:hover {
  background-color: #0056b3;
}

@media (max-width: 768px) {
  .movie-detail-info {
    grid-template-columns: 1fr;
  }
}
</style>
