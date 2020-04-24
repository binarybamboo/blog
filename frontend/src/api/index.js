import axios from "axios";
const url = "http://127.0.0.1:8000/";

const api = {
  register: url + "users/register/",
  user: url + "users/",
  login: url + "auth/",
  refresh: url + "auth/refresh/",
  verify: url + "auth/verify/",
  boardlist: url + "board/list/",
  board: url + "board/",
  category: url + "board/category/",
};

function fetchLogin(obj) {  // 로그인 
  return axios.post(api.login, obj);
}
function fetchSignup(obj) { // 회원가입
  return axios.post(api.register, obj);
}
function fetchMemberinfo(token) { // 토큰으로 멤버 정보 가져오기 
  return axios.get(api.user, { headers: { Authorization: "jwt " + token } });
}
function fetchList(param) { // 게시글 목록 
  return axios.get(api.boardlist + param + "/");
}
function fetchList2(param) { // 카테고리별 검색
  return axios.get(api.category + param.name + "/" + param.id + "/");
}
function fetchBoard(param) { // 게시글 
  return axios.get(api.board + param);
}
function fetchCategory() { // 카테고리 검색
  return axios.get(api.category);
}
export {
  fetchLogin,
  fetchSignup,
  fetchMemberinfo,
  fetchList,
  fetchBoard,
  fetchCategory,
  fetchList2,
};
