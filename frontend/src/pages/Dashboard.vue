<template>
  <q-page class="q-pa-md">
    <div class="row q-gutter-md justify-between">
      <div v-for="memory in memories" :key="memory.key" class="memory-container" @click="carousel = true">
        <img v-if="memory.type == 'image'" class="memory-image" :src="memory.image" />
        <div v-if="memory.type == 'story'" class="memory-image">{{ memory.story }}</div>
        <div v-if="memory.type == 'video'" class="memory-container" ><q-avatar icon="ondemand_video" color="primary" text-color="white" />{{ memory.video }}</div>
        <div v-if="memory.type == 'audio'" class="memory-container" ><q-avatar icon="headset" color="primary" text-color="white" />{{ memory.audio }}</div>
      </div>
    </div>

    <q-dialog v-model="carousel">
      <q-carousel
        transition-prev="slide-right"
        transition-next="slide-left"
        swipeable
        animated
        v-model="slide"
        control-color="primary"
        navigation-icon="radio_button_unchecked"
        navigation
        padding
        height="200px"
        class="bg-white shadow-1 rounded-borders"
      >
        <q-carousel-slide :name="1" class="column no-wrap flex-center">
          <q-icon name="style" color="primary" size="56px" />
          <div class="q-mt-md text-center">
            lorem
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="2" class="column no-wrap flex-center">
          <q-icon name="live_tv" color="primary" size="56px" />
          <div class="q-mt-md text-center">
            lorem
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="3" class="column no-wrap flex-center">
          <q-icon name="layers" color="primary" size="56px" />
          <div class="q-mt-md text-center">
            lorem
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="4" class="column no-wrap flex-center">
          <q-icon name="terrain" color="primary" size="56px" />
          <div class="q-mt-md text-center">
            lorem
          </div>
        </q-carousel-slide>
      </q-carousel>
    </q-dialog>

    {{ memories }}
  </q-page>
</template>

<style scoped>
  .memory-container {
    width: 250px;
    height: 250px;
    border: 1px solid black;
  }
  .memory-image {
    max-width: 100%;
    max-height: 100%;
  }
</style>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import ReviewNoteTable from '../components/ReviewNoteTable.vue';
import PerformanceReviewTable from '../components/PerformanceReviewTable.vue';
import { PerformanceReviewRetrieve } from '../store/types'

@Component({
  components: { PerformanceReviewTable, ReviewNoteTable }
})
export default class Dashboard extends Vue {
  private currentIndex = -1
  private title = ''
  private memories = []
  private carousel = false
  private slide = 1

  private images() {
    let images = this.$store.getters['memoriesModule/images'].results // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
    images.forEach(image => {
      image.key = `image-${image.pk}`
      image.type = 'image'
    })
    return images
  }

  private stories() {
    let stories = this.$store.getters['memoriesModule/stories'].results // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
    stories.forEach(story => {
      story.key = `story-${story.pk}`
      story.type = 'story'
    })
    return stories
  }

  private videos() {
    let videos = this.$store.getters['memoriesModule/videos'].results // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
    videos.forEach(video => {
      video.key = `video-${video.pk}`
      video.type = 'video'
    })
    return videos
  }

  private audio() {
    let audio = this.$store.getters['memoriesModule/audio'].results // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
    audio.forEach(audio => {
      audio.key = `audio-${audio.pk}`
      audio.type = 'audio'
    })
    return audio
  }

  private getMemories() {
    let memories = []
    Promise.all([
      this.$store.dispatch('memoriesModule/getImages'),
      this.$store.dispatch('memoriesModule/getStories'),
      this.$store.dispatch('memoriesModule/getVideos'),
      this.$store.dispatch('memoriesModule/getAudio')
    ]).then(() => {
      this.images().forEach(imageMemory => memories.push(imageMemory))
      this.stories().forEach(storyMemory => memories.push(storyMemory))
      this.videos().forEach(videoMemory => memories.push(videoMemory))
      this.audio().forEach(audioMemory => memories.push(audioMemory))
      this.memories = memories
        .map((a) => ({sort: Math.random(), value: a}))
        .sort((a, b) => a.sort - b.sort)
        .map((a) => a.value)
    });
  }



  
  private isManager(): boolean {
    return this.$store.getters['userModule/getEmployeeProfile'].is_manager // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
  }

  private isUpperManager(): boolean {
    return this.$store.getters['userModule/getEmployeeProfile'].is_upper_manager // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
  }

  private isTheHRManager(): boolean {
    return this.$store.getters['userModule/getEmployeeProfile'].is_hr_manager // eslint-disable-line
  }

  private isTheExecutiveDirector(): boolean {
    return this.$store.getters['userModule/getEmployeeProfile'].is_executive_director // eslint-disable-line
  }

  private getNextReview(): PerformanceReviewRetrieve {
    return this.$store.getters['performanceReviewModule/nextPerformanceReview'] // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
  }

  private nextReviewNeedsEvaluation(): boolean {
    return this.getNextReview().status == 'Needs evaluation'
  }

  private userSignedNextEvaluation(): boolean {
    // Return if there is a date for the employee's signature on the review
    if (this.getNextReview().all_required_signatures) {
      return !!this.getNextReview().all_required_signatures[0][2]
    } else {
      return false
    }
  }

  private viewReview(pk: number): void {
    this.$router.push(`pr/${ pk }`)
      .catch(e => {
        console.error('Error navigating to PR detail', e)
      })
  }

  mounted() {
    // this.retrieveImages()
    //   .catch(e => {
    //     console.error('Error retrieving images:', e)
    //   })
    this.getMemories()
  }
};
</script>
