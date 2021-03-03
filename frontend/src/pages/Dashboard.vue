<template>
  <q-page class="q-pa-md">
    <div class="row q-gutter-md justify-between">
      <div v-for="image in images()" :key="image.pk" class="memory-container" ><img class="memory-image" :src="image.image" /></div>
      <div v-for="image in images()" :key="image.pk" class="memory-container" ><img class="memory-image" :src="image.image" /></div>
      <div v-for="image in images()" :key="image.pk" class="memory-container" ><img class="memory-image" :src="image.image" /></div>
    </div>
    {{ images() }}
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
import { ImageRetrieve, PerformanceReviewRetrieve } from '../store/types'

@Component({
  components: { PerformanceReviewTable, ReviewNoteTable }
})
export default class Dashboard extends Vue {
  private currentIndex = -1
  private title = ''
  // private images: Array<ImageRetrieve> = []

  private images() {
    return this.$store.getters['memoriesModule/images'].results
  }
  
  // private retrieveImages() {
  //   return new Promise((resolve, reject) => {
  //     this.$store.dispatch('userModule/getAllImages')
  //       .then(() => {
  //         this.images = this.$store.getters['userModule/getAllImages'] // eslint-disable-line
  //         console.log(this.images)
  //         resolve()
  //       })
  //       .catch(e => {
  //         console.error('Error retrieving Images from API:', e)
  //         reject(e)
  //       })
  //   })
  // }

  // private getAllImages(): ImageRetrieve {
  //   debugger
    
  //   return this.$store.getters['userModule/getAllImages'] // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
  // }
  
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
  }
};
</script>
