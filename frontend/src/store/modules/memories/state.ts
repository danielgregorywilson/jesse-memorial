export interface Image {
  pk: number
  image: string
}

export interface Story {
  pk: number
  story: string
}

export interface Video {
  pk: number
  video: string
}

export interface Audio {
  pk: number
  audio: string
}

export interface MemoriesStateInterface {
  images: Array<Image>
  stories: Array<Story>
  videos: Array<Video>
  audio: Array<Audio>
}

const state: MemoriesStateInterface = {
  images: [],
  stories: [],
  videos: [],
  audio: [],
};

export default state;
