import { GetterTree } from 'vuex';
import { StateInterface } from '../../index';
import { MemoriesStateInterface } from './state';

const getters: GetterTree<MemoriesStateInterface, StateInterface> = {
  images: state => state.images,
  nextPerformanceReview: state => state.nextPerformanceReview,
  allReviewNotes: state => state.allReviewNotes,
  performanceReview: state => state.performanceReview,
  performanceReviewDetails: state => state.performanceReviewDetails, // TODO: Use this instead of performanceReview
  allPerformanceReviews: state => state.allPerformanceReviews,
  allPerformanceReviewsActionRequired: state => state.allPerformanceReviewsActionRequired,
  allPerformanceReviewsActionNotRequired: state => state.allPerformanceReviewsActionNotRequired,
  allSignaturePerformanceReviewsActionRequired: state => state.allSignaturePerformanceReviewsActionRequired,
  allSignaturePerformanceReviewsActionNotRequired: state => state.allSignaturePerformanceReviewsActionNotRequired,
};

export default getters;
