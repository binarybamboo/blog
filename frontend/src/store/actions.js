/* eslint-disable */
import {
  fetchLogin,
  fetchSignup,
  fetchMemberinfo,
  fetchList,
  fetchList2,
  fetchBoard,
  fetchCategory,
} from "../api/index.js";
import router from "../routes/index.js";

export default {
  async FETCH_LOGIN({ commit }, obj) {
    try {
      const response = await fetchLogin(obj);
      console.log(response.data);
      commit("SET_LOGIN", response.data);
      alert("로그인이 완료되었습니다.");
      this.dispatch("getMemberInfo");
      router.push({ name: "board" });
    } catch (error) {
      console.log(error);
    }
  },
  async FETCH_SIGNUP({ commit }, obj) {
    try {
      const response = await fetchSignup(obj);
      console.log(response.data);
      alert("회원가입이 완료되었습니다.");
      router.push({ name: "login" });
    } catch (error) {
      console.log(error);
    }
  },
  async FETCH_LOGOUT({ commit }) {
    try {
      sessionStorage.removeItem("access_token");
      commit("SET_LOGOUT");
      alert("로그아웃이 완료되었습니다.");
      router.push({ name: "board" });
    } catch (error) {
      console.log(error);
    }
  },
  async getMemberInfo({ commit }) {
    try {
      let token = sessionStorage.getItem("access_token");
      //토큰 -> 멤버 정보 반환
      // 새로고침 --> 토큰만 갖고 멤버 정보 요청 가능
      const response = await fetchMemberinfo(token);
      console.log(response);
      commit("SET_REFRESH", response.data);
      return response;
    } catch (error) {
      console.log(error);
    }
  },

  async FETCH_LIST({ commit }, params) { // 게시글 목록 
    try {
      const response = await fetchList(params);
      console.log(response.data);
      commit("SET_LIST", response.data);
      return response;
    } catch (error) {
      console.log(error);
    }
  },
  async FETCH_LIST2({ commit }, params) { // 카테고리별 게시글보기
    try {
      const response = await fetchList2(params);
      console.log(response.data);
      commit("SET_LIST", response.data);
      return response;
    } catch (error) {
      console.log(error);
    }
  },
  async FETCH_BOARD({ commit }, params) { // 게시글 
    try {
      const response = await fetchBoard(params);
      console.log(response.data);
      commit("SET_BOARD", response.data);
      return response;
    } catch (error) {
      console.log(error);
    }
  },
  async FETCH_CATEGORY({ commit }) { //카테고리별 검색 
    try {
      const response = await fetchCategory();
      console.log(response.data);
      commit("SET_CATEGORY", response.data);
      return response;
    } catch (error) {
      console.log(error);
    }
  },
};
