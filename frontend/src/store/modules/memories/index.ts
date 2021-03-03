import { Module } from 'vuex';
import { StateInterface } from '../../index';
import state, { MemoriesStateInterface } from './state';
import actions from './actions';
import getters from './getters';
import mutations from './mutations';

const memoriesModule: Module<MemoriesStateInterface, StateInterface> = {
  namespaced: true,
  actions,
  getters,
  mutations,
  state
};

export default memoriesModule;
