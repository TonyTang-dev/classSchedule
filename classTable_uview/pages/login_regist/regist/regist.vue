<template>
	<view class="content">
		
		<!-- 背景图片 -->
		<image class="bgimg"></image>
		
		<view class="inputname">
			<u--input
				placeholder="请输入您的手机号"
				prefixIcon="phone"
				class="input-uvie"
				prefixIconStyle="font-size: 24px;color: #909399"
				v-model="registerPhone" >
			</u--input>
		</view>
		<view class="inputname">
			<u-input placeholder="请输入验证码"
			prefixIcon="bell"
			class="input-uvie"
			v-model="registerCode"
			maxlength="6"
			prefixIconStyle="font-size: 24px;color: #909399">
				<view slot="suffix">
					<u-button
						@tap="getsmscode"
						:text="smsbtn.text"
						type="success"
						size="mini"
					></u-button>
				</view> 
			</u-input> 
		</view>
		<view class="inputname">
			<u--input
				placeholder="请输入您的密码"
				prefixIcon="lock"
				class="input-uvie"
				:type="eyePass1"
				v-model="registerPassword"
				prefixIconStyle="font-size: 24px;color: #909399">
				<view slot="suffix">
					<u-icon v-if="lock1==true" name="eye-off" @click="changeEye(1)"></u-icon>
					<u-icon v-else name="eye-fill" @click="changeEye(1)"></u-icon>
				</view>
			</u--input>
		</view>
		<view class="inputname">
			<u--input
				placeholder="再次输入您的密码"
				prefixIcon="lock"
				suffixIcon="eye-fill"
				class="input-uvie"
				:type="eyePass2"
				v-model="confirmPassword"
				prefixIconStyle="font-size: 24px;color: #909399">
				<view slot="suffix">
					<u-icon v-if="lock2==true" name="eye-off" @click="changeEye(2)"></u-icon>
					<u-icon v-else name="eye-fill" @click="changeEye(2)"></u-icon>
				</view>
			</u--input>
		</view>
		<view style="padding: 0 10%; font-size: 14px;">
			<text style="color: red;">{{message}}</text>
		</view>
		<view class="buttonSet">
			<u-button @click="submit" class="button-LogReg">注册</u-button>
		</view>
	</view>
</template>

<script>
	//导入md5加密包
	import w_md5 from "../../../js_sdk/zww-md5/w_md5.js"
	export default {
		data() {
			return {
				userName:'',					//用户名
				userRootKey:'',					//用户权限密钥
				userAge:'',						//用户年龄
				userEmail:'',					//用户邮箱
				userGender:'',					//用户性别
				userPassword:'',				//用户密码
				userPpassword:'',				//用户第二次去人密码
				index:-1,						//下拉索引
				
				
				//2
				registerPhone: '',
				registerPassword: '',
				confirmPassword: '',
				registerCode: '',
				smsbtn: {
					text: '发送',
					status: false,
					codeTime: 60
				},
				timerId: null,
				message: '',
				
				// 小眼睛
				eyePass1: 'password',
				eyePass2: 'password',
				lock1: false,
				lock2: false,
			}
		},
		
		computed: {	
			
		},
		
		components: {
			
		},
		methods: {
			onLoad(){
				
			},
			
			//小眼睛
			changeEye(index){
				if(index==1){
					if(this.lock1){
						this.lock1=false;
						this.eyePass1="password"
					}
					else{
						this.lock1=true;
						this.eyePass1="text"
					}
				}
				else{
					if(this.lock2){
						this.lock2=false;
						this.eyePass2="password"
					}
					else{
						this.lock2=true;
						this.eyePass2="text"
					}
				}
			},
			
			//2
			getsmscode() {
				//此处写发送验证码逻辑
				if (this.smsbtn.codeTime != 60) {
					return;
				}
				this.timerId = setInterval(() => {//此处直接复制了另一个插件里的计时器，在插件市场里搜索登录，时间最靠前的那位
						let codeTime = this.smsbtn.codeTime;
						codeTime--;
						this.smsbtn.codeTime = codeTime;
						this.smsbtn.text = codeTime + "S";
						if (codeTime < 1) {
							clearInterval(this.timerId);
							this.smsbtn.text = "重试";
							this.smsbtn.codeTime = 60;
							this.smsbtn.status = false;
						}
					},
					1000);
				return false;
			},
			submit() {
				let registerPhone = this.registerPhone;
				let registerPassword = this.registerPassword;
				let confirmPassword = this.confirmPassword;
				let registerCode = this.registerCode;
				if (!(/^1(3|4|5|6|7|8|9)\d{9}$/.test(registerPhone))) {
					this.message = "手机号码有误/为空，请重填";
					return false;
				}
				if (registerCode < 100000) {
					this.message = "验证码不符合格式";
					return false;
				}
				if (!registerPassword) {
					this.message = "密码为空";
					return false;
				}
			
				let ls = 0;
				if (registerPassword.match(/([a-z])+/)) {
					ls++;
				}
				if (registerPassword.match(/([0-9])+/)) {
					ls++;
				}
				if (registerPassword.match(/([A-Z])+/)) {
					ls++;
				}
				if (registerPassword.match(/[^a-zA-Z0-9]+/)) {
					ls++;
				}
				if (registerPassword.length < 8) {
					ls = 0;
				}
				if (ls < 2) {
					this.message = "密码强度不够，至少8位，大写、小写、字母、符号 其中两种";
					return false;
				}
			
			
				if (confirmPassword != registerPassword) {
					this.message = "两次密码不同";
					return false;
				}
				uni.showLoading({
					title: '加载中。。。',
					mask: false
				});
			
				let headers = {};
				headers['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8';
				let PHPSESSID = uni.getStorageSync('PHPSESSID');
				if (PHPSESSID) {
					headers['cookie'] = 'PHPSESSID=' + PHPSESSID;//将PHPSESSID放入请求头中,如你有其他cookies都可以缀后面，分号分割。浏览器端本身就有cookies机制，不设置
				}
				
				return;//先直接杀掉网络请求
				
				
				uni.request({
					url: this.$url + '/api/login/register.php',//此处使用了全局变量拼接url（main.js文件中），关于全局变量官方问答里有
					method: 'POST',
					header: headers,
					data: {
						phone: this.registerPhone, //phone应该以后台验证码接收到的为phone，否则会造成修改后任意手机号注册漏洞，本demo不作处理
						pw: this.registerPassword //本demo没有传输验证码，自行传输
					},
					success: res => {
						console.log(res);
						let cookies = res.cookies;
						if (cookies) {
							for (let i = 0; i < cookies.length; i++) {
								if (cookies[i].name == 'PHPSESSID') {//PHPSESSID从cookies取出，放入本地储存
									uni.setStorageSync('PHPSESSID', cookies[i].value);
									break;
								}
							}
						}
						//返回的基本信息做本地缓存
						let data = res.data;
						if (data.ec === 0) {
							uni.setStorageSync('userinfo', data.user);
							uni.hideLoading();
							uni.reLaunch({
								url: '../index/indexme'
							});
						} else {
							uni.removeStorageSync('userinfo');
							this.message = data.msg;
							uni.hideLoading();
						}
					},
					fail: () => {
						uni.hideLoading();
						this.message = "网络连接失败";
					},
					complete: () => {}
				});
			},
			openAgreement() {
				uni.navigateTo({
					url: '../login/userAgreement',
					success: res => {},
					fail: () => {},
					complete: () => {}
				});
			}
		},
	};
</script>

<style lang="scss" scoped>
	// page{
	// 	background-color: #00f4b3;
	// }
	/* 背景图片 */
	.bgimg{
		background-image: url("../../../static/bgSky.png");
		// background-color: #5BC9C0;
		z-index: -1;
		width: 100%;
		height: 100%;
		position: fixed;
		// filter: blur(3rpx) brightness(70%);//模糊半径和变暗度
	}
	.content {						//父容器
		flex-direction: column;
		display: flex;
		align-items: center;
		align-content: center;
		width: 100%;
		height: 100%;
		
		.buttonSet{				//按钮集合设置
			width: 100%;
			flex-direction: row;
			display: flex;
			margin-top: 80rpx;
		}
		.button-LogReg{
			width: 60%;
			height: 35px;
			font-size: 16px;
			font-weight: bold;
			color: #5E5E5E;
		}
		.inputname {			//输入框用户名
			width: 70%;
			flex-direction: row;
			display: flex;
			align-items: center;
			justify-content: center;
			margin-top: 60rpx;
			font-weight: bold;
			
			.userName{			//用户名
				width: 100%;
				height: 2em;
				border-radius: 3px;
				background-color: #FFFFFF;
				font-size: 16px;
				color: #000000;
			}
			.icon{
				width: 24px;
				height: 24px;
				margin-right: 10rpx;
			}
			.userPassword{		//密码
				width: 100%;
				height: 2em;
				background-color: #FFFFFF;
				border-radius: 3px;
				font-size: 16px;
				color: #000000;
			}
		}
		
									//输入框设置
		input {
			text-align: left;
			margin-bottom: 5rpx;
			padding-bottom: 6rpx;
		}
	}
	
	// 验证码
	.code-input{
		flex: 1;
		border-style: none;
		font-weight: bold;
	}
	.getcode{
		width: 3em;
		padding-left: 3rpx;
		font-size: 16px;
		border-style: none  none none solid;
		border-width: 1px;
		border-color: #999791;
		opacity: 0.8;
	}
	.eye{
		width: 24px;
		height: 24px;
	}
	
	.input-uvie{
		font-weight: bold;
		font-size: 16px;
		background-color: #FFFFFF; 
	}
</style>
