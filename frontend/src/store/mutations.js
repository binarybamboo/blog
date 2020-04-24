export default {
  SET_LOGIN(state, info) {
    let token = info.token;
    sessionStorage.setItem("access_token", token);
    state.isLogin = true;
  },
  SET_LOGOUT(state) {
    state.userInfo = null;
    state.isLogin = false;
  },
  SET_REFRESH(state, info) {
    state.userInfo = info;
    state.isLogin = true;
  },
  SET_LIST(state, info) {
    state.list = info;
  },
  SET_BOARD(state, info) {
    state.board = info;
  },
  SET_CATEGORY(state, info) {
    state.category = info;
  },
};
