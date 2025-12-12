<template>
  <div class="youtube-card" @click="$emit('play-video', video.id.videoId)">
    <img :src="thumbnailUrl" :alt="video.snippet.title" class="thumbnail">
    <div class="video-info">
      <h3 class="video-title">{{ video.snippet.title }}</h3>
      <p class="channel-name">{{ video.snippet.channelTitle }}</p>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  video: {
    type: Object,
    required: true
  }
})

defineEmits(['play-video'])

const thumbnailUrl = computed(() => {
  return props.video.snippet.thumbnails.medium.url
})
</script>

<style scoped>
.youtube-card {
  background-color: white;
  border: 1px solid #ddd;
  cursor: pointer;
}

.youtube-card:hover {
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.thumbnail {
  width: 100%;
  height: 180px;
  object-fit: cover;
}

.video-info {
  padding: 12px;
}

.video-title {
  font-size: 0.95rem;
  margin-bottom: 8px;
  color: #333;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.3;
}

.channel-name {
  color: #666;
  font-size: 0.85rem;
}
</style>
