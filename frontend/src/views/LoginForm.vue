  
<template>
	<div>
		<login-form></login-form>
	</div>
</template>

<script>
import LoginForm from '../components/LoginForm.vue'
import router from '../routes/index.js'
export default {
	mounted() {
	},
	beforeCreate(){
		const token=sessionStorage.getItem("access_token");
		if(token){
			router.push({name:"WhiteBoard"})
		}
	},
	components:{
		LoginForm
	},
   
};
</script>

<style scoped>

</style>