import Vue from "vue";
import VueRouter from "vue-router";

//component import
import WhiteBoard from "../views/WhiteBoard.vue";
import LoginForm from "../views/LoginForm.vue";
import BoardView from "../views/BoardView.vue";
import SignupForm from "../views/SignupForm.vue";
Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  routes: [
    {
      path: "",
      redirect: "/list/1",
    },
    {
      path: "/list/:id",
      name: "board",
      component: WhiteBoard,
    },
    {
      path: "/login",
      name: "login",
      component: LoginForm,
    },
    {
      path: "/signup",
      name: "signup",
      component: SignupForm,
    },
    {
      path: "/board/:id",
      name: "boardview",
      component: BoardView,
    },
    {
      path: "/category/:name/:id",
      name: "category",
      component: WhiteBoard,
    },
  ],
});
