import { AudioRetrieve, ImageRetrieve, StoryRetrieve, VideoRetrieve } from 'src/store/types'
import Vue from 'vue'

import { MutationTree } from 'vuex'
import { MemoriesStateInterface } from './state'


const mutation: MutationTree<MemoriesStateInterface> = {
  setImages: (state, resp: {data: ImageRetrieve}) => {
    Vue.set(state, 'images', resp.data)
  },
  setStories: (state, resp: {data: StoryRetrieve}) => {
    Vue.set(state, 'stories', resp.data)
  },
  setVideos: (state, resp: {data: VideoRetrieve}) => {
    Vue.set(state, 'videos', resp.data)
  },
  setAudio: (state, resp: {data: AudioRetrieve}) => {
    Vue.set(state, 'audio', resp.data)
  },
};

export default mutation;
