<template>
  <Teleport to="body">
    <div v-if="isOpen" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <button class="close-btn" @click="closeModal">&times;</button>
        <h2>{{ title }}</h2>
        <div v-if="loading" class="loading">
          <p>영상을 불러오는 중...</p>
        </div>
        <div v-else-if="error" class="error">
          <p>{{ error }}</p>
        </div>
        <div v-else-if="videoId" class="video-container">
          <iframe
            :src="`https://www.youtube.com/embed/${videoId}`"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          ></iframe>
        </div>
        <div v-else class="no-video">
          <p>예고편을 찾을 수 없습니다.</p>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script setup>
import { ref, watch } from 'vue'
import axios from 'axios'

const props = defineProps({
  isOpen: {
    type: Boolean,
    required: true
  },
  movieTitle: {
    type: String,
    default: ''
  },
  title: {
    type: String,
    default: '영화 예고편'
  }
})

const emit = defineEmits(['close'])

const videoId = ref(null)
const loading = ref(false)
const error = ref(null)

const searchTrailer = async () => {
  if (!props.movieTitle) return

  try {
    loading.value = true
    error.value = null
    const apiKey = import.meta.env.VITE_YOUTUBE_API_KEY

    const response = await axios.get('https://www.googleapis.com/youtube/v3/search', {
      params: {
        key: apiKey,
        q: `${props.movieTitle} official trailer`,
        part: 'snippet',
        type: 'video',
        maxResults: 1
      }
    })

    if (response.data.items && response.data.items.length > 0) {
      videoId.value = response.data.items[0].id.videoId
    } else {
      error.value = '예고편을 찾을 수 없습니다.'
    }
  } catch (err) {
    console.error('유튜브 검색 중 오류 발생:', err)
    error.value = '영상을 불러오는데 실패했습니다.'
  } finally {
    loading.value = false
  }
}

watch(() => props.isOpen, (newVal) => {
  if (newVal && props.movieTitle) {
    searchTrailer()
  } else {
    videoId.value = null
    error.value = null
  }
})

const closeModal = () => {
  emit('close')
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: white;
  border-radius: 5px;
  padding: 20px;
  max-width: 700px;
  width: 90%;
  position: relative;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 15px;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #333;
}

.close-btn:hover {
  color: #007bff;
}

h2 {
  margin-bottom: 15px;
  color: #333;
}

.video-container {
  position: relative;
  padding-bottom: 56.25%;
  height: 0;
  overflow: hidden;
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.loading,
.error,
.no-video {
  text-align: center;
  padding: 30px;
}

.error {
  color: red;
}
</style>
