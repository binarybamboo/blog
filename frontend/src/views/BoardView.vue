<template>
  <div>
    <board-view></board-view>
  </div>
</template>

<script>
/* eslint-disable */
import BoardView from '../components/BoardView.vue'
export default {
  beforeCreate() {  
          try {
              
              this.$store.dispatch("FETCH_BOARD",this.$route.params.id);
              let disqus_config = function () {
                  this.page.url = location.origin;
                  this.page.identifier = location.pathname;
              };
      // blog-e8wjypjjjl
              (function () {
                  let d = document, s = d.createElement('script');
                  s.src = 'https://jmboard.disqus.com/embed.js';
                  s.setAttribute('data-timestamp', +new Date());
                  (d.head || d.body).appendChild(s);
              })();
          } catch (e) {
              // some error
          }
        },
    mounted() {
      
    },
    computed:{
      params(){return this.$route.params.id;}
    },
    watch:{
    params :function(newVal){
        this.$store.dispatch("FETCH_BOARD",newVal);
        
      }
    }
    ,
    components:{
        BoardView
    }
}
</script>

<style>

</style>