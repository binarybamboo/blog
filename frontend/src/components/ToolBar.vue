<template>
  <div class='header'>
      <!-- JM BOARD LOGO 왼쪽에,  -->
      <div class="logo">
        <router-link to="/"><img :src="images.sample" /></router-link>
      </div>
      <!-- 유저 info-->
    <div class="info" v-if="isLogin">
      <img :src="src" />
      {{userInfo.nickname}}
      <b-dropdown size="lg"  variant="link" toggle-class="text-decoration-none" no-caret>
        <template v-slot:button-content>
          &#128071;<span class="sr-only">Search</span>
        </template>
            <b-dropdown-item @click="FETCH_LOGOUT">logout</b-dropdown-item>
      </b-dropdown>
      
    </div>
    <div class='info' v-else>
        <b-button variant="light"><router-link to="/login/">Login</router-link></b-button>
    </div>
    <div style='clear:both'></div>
  </div>
</template>

<script>
import {mapState,mapActions} from 'vuex';
export default {
  data(){
    return{
      images: {
                sample: require('@/assets/logo.png')
            }
    }
  },
  computed:{
    ...mapState(['userInfo','isLogin','isLoginError']),
    src(){
      if(this.isLogin){
        return "https://api.adorable.io/avatars/30/"+this.userInfo.nickname+ ".png/";
      }
      return "https://api.adorable.io/avatars/30/asd.png";
    }
  },
  methods:{
    ...mapActions(['FETCH_LOGOUT'])
  }
}
</script>

<style scoped>
.header{
        min-height: 50px;
        color:white;
        background-color:#5383e8;
        padding:8px;
}
.header .router-link-exact-active{
     color: #35495e;
}
.logo img{
    margin-left:10px;
    float:left;
}
.info{
  display:inline-block;
  float:right;
  padding:0 20px 0px;
  vertical-align:middle;
}
.info img{
  border-radius: 20px;
  margin-right:2px;
  
}
</style>