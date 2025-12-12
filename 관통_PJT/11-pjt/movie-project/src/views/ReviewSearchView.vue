<template>
  <div class="review-search">
    <h1>영화 리뷰 영상 검색</h1>

    <form @submit.prevent="searchReviews" class="search-form">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="영화 제목을 입력하세요"
        class="search-input"
      >
      <button type="submit" class="search-btn">검색</button>
    </form>

    <div v-if="loading" class="loading">
      <p>리뷰 영상을 검색 중...</p>
    </div>

    <div v-else-if="error" class="error">
      <p>{{ error }}</p>
    </div>

    <div v-else-if="videos.length > 0" class="videos-grid">
      <YoutubeCard
        v-for="video in videos"
        :key="video.id.videoId"
        :video="video"
        @play-video="playVideo"
      />
    </div>

    <div v-else-if="searched && videos.length === 0" class="no-results">
      <p>검색 결과가 없습니다.</p>
    </div>

    <YoutubeReviewModal
      :is-open="showModal"
      :video-id="selectedVideoId"
      @close="showModal = false"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import YoutubeCard from '../components/YoutubeCard.vue'
import YoutubeReviewModal from '../components/YoutubeReviewModal.vue'

const searchQuery = ref('')
const videos = ref([])
const loading = ref(false)
const error = ref(null)
const searched = ref(false)
const showModal = ref(false)
const selectedVideoId = ref('')

const searchReviews = async () => {
  if (!searchQuery.value.trim()) {
    error.value = '검색어를 입력해주세요.'
    return
  }

  try {
    loading.value = true
    error.value = null
    searched.value = true
    const apiKey = import.meta.env.VITE_YOUTUBE_API_KEY

    const response = await axios.get('https://www.googleapis.com/youtube/v3/search', {
      params: {
        key: apiKey,
        q: `${searchQuery.value} 영화 리뷰`,
        part: 'snippet',
        type: 'video',
        maxResults: 12
      }
    })

    videos.value = response.data.items
  } catch (err) {
    console.error('유튜브 검색 중 오류 발생:', err)
    error.value = '리뷰 영상을 검색하는데 실패했습니다.'
  } finally {
    loading.value = false
  }
}

const playVideo = (videoId) => {
  selectedVideoId.value = videoId
  showModal.value = true
}
</script>

<style scoped>
.review-search {
  padding: 20px 0;
}

h1 {
  font-size: 1.8rem;
  margin-bottom: 20px;
}

.search-form {
  display: flex;
  gap: 10px;
  margin-bottom: 30px;
  max-width: 600px;
}

.search-input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 3px;
  font-size: 1rem;
}

.search-input:focus {
  outline: none;
  border-color: #007bff;
}

.search-btn {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.search-btn:hover {
  background-color: #0056b3;
}

.loading,
.error,
.no-results {
  text-align: center;
  padding: 40px 0;
}

.error {
  color: red;
}

.videos-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}
</style>
