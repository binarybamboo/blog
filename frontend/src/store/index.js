import Vue from "vue";
import Vuex from "vuex";
import getters from "./getters.js";
import mutations from "./mutations.js";
import actions from "./actions.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userInfo: [],
    isLogin: false,
    list: [],
    board: [],
    category: [],
  },
  getters,
  mutations,
  actions,
});
