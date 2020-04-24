<template>
  <div>
    <!-- 게시글 테이블  -->
    <div class="wrap" >
      <b-table
      :striped="striped"
      :hover="hover"
      :items="calItems"
      :fields="fields"
    >
    <template v-slot:cell(title)="data">
        <router-link :to="'/board/'+data.item.id+'/'">{{data.value}}</router-link>
      </template>
    </b-table>
    </div>
    <!-- 카테로그 창  -->
    <div calss='category' v-if="category">
      <strong>분류</strong>
    <b-list-group>
      <b-list-group-item class="d-flex justify-content-between align-items-center" v-for="cate in category" :key="cate.id">
        <router-link :to="{name :'category',params:{name: cate.name,id:1}}">{{cate.name}}</router-link>
        <b-badge variant="primary" pill>{{cate.post_num}}</b-badge>
      </b-list-group-item>
    </b-list-group>
    </div>
  <div class='clear'></div>
    <!-- pagination -->
    <div class="mt-3">
      <b-pagination-nav pills size="lg" number-of-pages="10" :link-gen="linkGen" align="center" use-router>
        
      </b-pagination-nav>
    </div>
  </div>
</template>

<script>
// this.$route.params.id
import { mapState} from 'vuex';
export default {
    data() {
      return {
        fields: ['id', 'title', 'author','created'],
        striped: true,
        hover: true,
        dark: true,
      }
    },
    methods: {
      linkGen(pageNum) {
        if(this.$route.name=="board")
         return `/list/${pageNum}/`;
        else
         return `/category/${this.$route.params.name}/${pageNum}`;
      },
    },
    computed:{
        ...mapState(['list','category']),
        calItems(){ //테이블의 데이터 값 대입 
          let items=[];
          for(let i=0;i<this.list.length;i++){
            let itemjson={
              'id':i+1,
              'title': this.list[i].title,
              'author':this.list[i].author,
              'created':this.list[i].created
            }
            items.push(itemjson);
          }
          return items;
        },
    },
    watch:{
      $route:function(newVal){
         if(this.$route.name=="board"){
          this.$store.dispatch("FETCH_LIST",newVal.params.id);
        }else if(this.$route.name=="category"){
          this.$store.dispatch("FETCH_LIST2",newVal.params);
        }
      },
    }
  }
</script>
<style scoped>
.wrap{
  float:left;width:80%;
}
b-list-group{
  float:right;width:20%;min-height:540px;
}
.mt-3{
  text-align:center
}
.clear{
  clear:both
}
</style>