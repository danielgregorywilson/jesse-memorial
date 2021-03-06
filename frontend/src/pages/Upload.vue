<template>
  <q-page class="q-pa-md">
    <div class="q-gutter-sm">
      <q-radio v-model="type" val="image" label="Image" />
      <q-radio v-model="type" val="story" label="Story" />
      <q-radio v-model="type" val="video" label="Video" />
      <q-radio v-model="type" val="audio" label="Audio" />
    </div>
    <!-- <input v-if="type != 'story'" type="file" id="file_upload" name="file_upload"> -->
    <q-file v-if="type != 'story'" v-model="file" :label="type" />
    <q-input
      v-if="type == 'story'"
      v-model="story"
      filled
      type="textarea"
    />
    <q-input v-model="title" label="Title" />
    <q-input v-model="description" label="Description" />
    <q-date
      v-model="date"
      minimal
    />
    <q-btn label="Upload" @click="upload()" :disable="!fieldsComplete()" />
  </q-page>
</template>

<style scoped>

</style>

<script lang="ts">
import axios from 'axios';
import { Component, Vue } from 'vue-property-decorator'
import ReviewNoteTable from '../components/ReviewNoteTable.vue';
import PerformanceReviewTable from '../components/PerformanceReviewTable.vue';

@Component({
  components: { PerformanceReviewTable, ReviewNoteTable }
})
export default class Dashboard extends Vue {
  private type = 'image'
  private title = ''
  private description = ''
  private date = ''

  private file = new File([''], '')
  private story = ''
  private successfulUpload = false

  private fieldsComplete(): boolean {
    return !!this.story || this.type != 'story'
  }

  private upload(): void {
    let fd = new FormData();
    fd.append('title', this.title)
    fd.append('description', this.description)
    if (!this.date) {
      this.date = ''
    }
    fd.append('date', this.date.split('/').join('-'))
    
    // const { type, title, description, date, file, story } = this
    switch(this.type) {
      case 'image':
        fd.append('image', this.file)
        axios({url: `${ process.env.API_URL }api/upload-image/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
          .then(() => {
            this.successfulUpload = true
          })
          .catch(e => {
            console.error('Error uploading image memory:', e)
          })
        break;
      case 'story':
        fd.append('story', this.story)
        axios({url: `${ process.env.API_URL }api/upload-story/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
          .then(() => {
            this.successfulUpload = true
          })
          .catch(e => {
            console.error('Error uploading story memory:', e)
          })
        break;
      case 'video':
        fd.append('video', this.file)
        axios({url: `${ process.env.API_URL }api/upload-video/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
          .then(() => {
            this.successfulUpload = true
          })
          .catch(e => {
            console.error('Error uploading video memory:', e)
          })
        break;
      case 'audio':
        fd.append('audio', this.file)
        axios({url: `${ process.env.API_URL }api/upload-audio/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
          .then(() => {
            this.successfulUpload = true
          })
          .catch(e => {
            console.error('Error uploading audio memory:', e)
          })
        break;
      default:
        // code block
    }
  }

};
</script>
