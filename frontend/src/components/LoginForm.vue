<template>
  <div id="login_wrapper">
		<h1>Welcome To LoginForm</h1>
		<div class="form">
			<div>
				<label for="email">이메일</label>
				<input type="text" id="email" maxlength="20" placeholder="email" v-model="email" required>
			</div>
			<div>
				<label for='pwd'>비밀번호</label>
				<input type="password" id="pwd" name="pwd" maxlength="20" v-model="password" placeholder="password" required>
			</div>
            
			<input type="submit" id="btn_login" @click="FETCH_LOGIN({email,password})" value="로그인">
            <input type="submit" id="btn_signup" value="회원가입" @click="move()" />
            
		</div>
	</div>  
</template>

<script>
import router from '../routes/index.js'
import {mapActions} from 'vuex';
export default {
    data(){
        return{
            email:'',
            password:'',
        }
    },
    methods:{
		...mapActions(['FETCH_LOGIN']),
		move(){
			router.push({name : 'signup'})
		}
    }
}
</script>

<style scoped>
#login_wrapper { 
	
	border-radius: 50px;
    border: 20px solid lightblue;
    padding: 5px 20px;
    position: absolute;
    top: 50%;
    left: 50%;
    width: 450px; height: 250px;
    margin-left: -220px;
    margin-top : -170px;
    
    display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
} 
h1{
	font-size: 25px;
	padding-bottom: 20px;
}
.form{
	width: 300px;
}
.form > div{
	display: flex;
	justify-content: center;
	padding-bottom: 7px;
	align-items: center;
}
label{
	flex: 1;
	text-align: left;
}
input[type="submit"]{
	width: 85px;
	float: right;
	padding: 3px;
}
input {
	padding: 5px;
}
input[type="submit"]{
    width:150px;
}

</style>