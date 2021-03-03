// TODO
interface ReviewNoteInterface {
  employee: unknown
  note: string
}

// TODO: Update to match shape of frontend/src.store/types/PerformanceReviewRetrieve
export interface PerformanceReviewInterface {
  pk?: number
  employee_pk?: number
  employee_name: string
  performance_period: string
  days_until_review: string
  status: string
  evaluation: string
}

export interface Image {
  pk: number
  image: string
}

export interface MemoriesStateInterface {
  images: Array<Image>
}

const state: MemoriesStateInterface = {
  images: [],
};

export default state;
