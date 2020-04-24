<template>
  <div>
      <WhiteBoard></WhiteBoard>
  </div>
</template>

<script>
import WhiteBoard from '../components/WhiteBoard.vue'
import bus from '../utils/bus.js';
export default {
  computed:{
    routeName(){
      return this.$route.name;
    }
  },

  mounted(){
    //  로케이션별로 분기 기본 게시판인가
    bus.$emit('off:progress');
    
    if(this.$route.name=="board"){
      if(this.$route.params.id==undefined)
       this.$route.params.id=1;
      this.$store.dispatch("FETCH_LIST",this.$route.params.id);
    }  // 그게 아니면 카테고리분기인가
    else if(this.$route.name=="category"){
      
      this.$store.dispatch("FETCH_LIST2",this.$route.params)
    }
    // 카테고리 불러오기
      this.$store.dispatch("FETCH_CATEGORY");
  },
  components:{
    WhiteBoard
  }
}
</script>

<style>

</style>