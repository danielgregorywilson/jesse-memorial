import { GetterTree } from 'vuex';
import { StateInterface } from '../../index';
import { MemoriesStateInterface } from './state';

const getters: GetterTree<MemoriesStateInterface, StateInterface> = {
  images: state => state.images,
  stories: state => state.stories,
  videos: state => state.videos,
  audio: state => state.audio,
};

export default getters;
