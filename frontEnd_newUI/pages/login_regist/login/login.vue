<template>
	<view class="content">		
		<!-- 背景图片 -->
		<image class="bgimg"></image>
		
		<image class="back" @click="back" src="../../../static/back.png"></image>
		
		
		<view class="title">
			<image class="loginGif" src="../../../static/login_logo.gif"></image>
			CQU课程表
		</view>
		<image class="logo" :src="myHeadPhoto"></image>
		<view class="inputname">
			<text class="hintName">用户名：</text>
			<input class="userName" @input="changeName" type="text" v-model="userName"  placeholder="请输入用户名" />
		</view>
		<view class="inputname">
			<text class="hintPassword">密   码：</text>
			<input class="userPassword" type="password" v-model="userPassword" placeholder="请输入密码" />
		</view>
		<view class="aboutpassword">
			<u-checkbox-group class="checkbox">
				<u-checkbox
					size="13px" 
					icon-size="12px"
					label="记住密码"
					label-size="12px"
					@change="checkboxChange"
					v-model="checked"
					:disabled="false">
				</u-checkbox>
			</u-checkbox-group>
			<text class="forget" @click="forgetpassword">忘记密码？</text>
		</view>
		<view class="buttonSet">
			<u-button @click="submit" :style="[buttonStyle]" class="button-LogReg">登录</u-button>
			<u-button @click="registButton" :style="[buttonStyle]" class="button-LogReg">注册</u-button>
		</view>
		<view class="loginAPI-wrap">
			<image class="loginAPI_icon" src="../../../static/QQ.png" @click="loginIII(1)"></image>
			<image class="loginAPI_icon" src="../../../static/weibo.png" @click="loginIII(2)"></image>
			<image class="loginAPI_icon" src="../../../static/wx.png" @click="loginIII(3)"></image>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				checked: false,		//记住密码复选框选中状态
				userName: '',		//用户名
				userPassword:'',	//用户密码
				myHeadPhoto:'',		//用户头像
				tempPhotoLink:'',
				tempUserName:'',
			}
		},
			
		computed: {					//按钮风格设定
			buttonStyle() {
				let style = {};
				style.color = "#fff";
				style.backgroundColor = this.$u.color['warning'];
				return style;
			},
		},
		
		components: {
			
		},
		
		methods: {
			changeName(e){
				var _this=this;
				if(e.target.value!=_this.tempUserName){
					_this.myHeadPhoto="/static/mine1.png"
				}
				else{
					_this.myHeadPhoto=_this.tempPhotoLink;
				}
			},
			
			onLoad(){				//创建页面时自动调用
				var _this=this
					
				uni.getNetworkType({//获取网络状态
					success(res) {
						if(res.networkType=="none"){
							// _this.$u.toast("您当前处于无网络状态，无法正常启动")
						}
						else if(res.networkType=="unknown"){
							// _this.$u.toast("您处于未知网络环境中");
						}
						else{
							// _this.$u.toast("您处于网络环境中");
						}
					},
					fail(e) {
						_this.$u.toast("无法获取您的网络状态");
					},
				});
					
				uni.getStorage({	//头像加载
					key:"headPhotoLink",
					success(e){
						if(e.data.Photolink!=""){
							_this.myHeadPhoto=e.data.Photolink
							_this.tempPhotoLink=e.data.Photolink
						}
						else{
							_this.myHeadPhoto="/static/mine1.png"
							_this.tempPhotoLink="/static/mine1.png"
							// _this.$u.toast("头像加载失败")
						}
					},
					fail(e){
						_this.myHeadPhoto="/static/head_man1.png"
						_this.tempPhotoLink="/static/mine1.png"
						// _this.$u.toast("头像加载失败")
					}
				})
			},
			onShow(){
				//this指针
				var _this=this
				
				uni.getStorage({		//打开页面则判断是否显示密码
					key:"userInfo",
					success(e){
						if(e.data.ischecked){	//如果是记住密码则自动填充密码
							_this.checked=e.data.ischecked
							_this.userName=e.data.name
							_this.tempUserName=e.data.name
							_this.userPassword=e.data.password
						}
						else{					//否则则置空
							_this.userName='';
							_this.userPassword='';
						}
					}
				})
			},
			
			checkboxChange(e) {					// 选中复选框时，由checkbox时触发
				this.checked=e.value
			},
			
			forgetpassword(){					//忘记密码
				uni.navigateTo({
					url:'forgetPassword/forgetPassword'
				})
			},
			
			//登录
			submit() {
				//this指针
				var _this=this;
				
				//判断状态
				if(_this.userName=="" || _this.userPassword==""){
					this.$u.toast("请先完善用户名和密码再登录")
					return
				}
				
				//检验密码位数是否符合要求
				if(this.userPassword.length!=6){
					this.$u.toast("您的密码格式不正确，请输入6位密码");
					return;
				}
				
				if(_this.checked==true){
					//缓存用户名密码
					uni.setStorage({
						key:"userInfo",
						data:{name:_this.userName,password:_this.userPassword,ischecked:_this.checked}
					})
				}
				else{
					//清除密码缓存
					uni.setStorage({
						key:"userInfo",
						data:{name:_this.userName,password:"",ischecked:_this.checked},
					})
				}
				
				//测试部分
				if(_this.userName == "admin" && _this.userPassword=="123456"){
					uni.switchTab({
						url:"../../navigate_page/Home/home"
					});
				}
				else{
					_this.$u.toast("账户或密码输入错误");
				}
				// return;//目前没有加入网络请求，先直接杀掉
				
				// this.$u.toast('发出登录请求')
				uni.request({
					// url: 'https://www.fastmock.site/mock/0063502729b0833db8e353ecf881960e/hair/login', 
					url: "/api/login",
					method:'GET',
					//加入请求头，完成表单传送
					// header: {
					//     'content-type': 'application/x-www-form-urlencoded'
					// },
					// data:{userName:_this.userName,password:_this.userPassword}, 
					success: (res) => {
						console.log(res)
						// if(!res.data.data.status){
						// 	_this.$u.toast("登录失败")
						// } 
						// else{
						// 	// console.log(res)
						// 	uni.setStorage({
						// 		key:"myKey",
						// 		data:{myKey:res.data.data.admin},
						// 	})
						// 	uni.switchTab({
						// 		url:"../../navigate_page/Home/home"
						// 	})
						// }
					}
				});
			},
			registButton(){			//注册
				uni.navigateTo({
					url:"../regist/regist"
				})
			},
			
			// 第三方登录按钮
			loginIII(index){
				var way="";
				index==1?way="QQ登录":index==2?way="微博登录":way="微信登录";
				this.$u.toast("点击了"+way);
			},
			
			// back
			back(){
				uni.navigateBack({
					delta:1,
				});
			}
		},
	};
</script>

<style lang="scss" scoped>
	page{						//全局页面配置
		// background-color: #f0f0f0;
	}
	/* 背景图片 */
	.bgimg{
		background-image: url("../../../static/bgSky.png");
		z-index: -1;
		width: 100%;
		height: 100%;
		position: fixed;
		filter: blur(3rpx) brightness(70%);//模糊半径和变暗度
	}
	
	.content {					//父容器
		flex-direction: column;
		display: flex;
		align-items: center;
		align-content: center;
		width: 100%;
		height: 100%;
		color: #FFFFFF;
		
		//gif图标
		.loginGif{
			width: 32px;
			height: 32px;
			border-radius: 5px;
		}
		
		.buttonSet{				//按钮集合设置
			flex-direction: row;
			display: flex;
		}
		.checkbox{				//复选框
			margin-top: 20px;
			color: #FFFFFF;
		}
		.logo {					//头像
			height: 72px;
			width: 72px;
			margin-top: 30rpx;
			margin-left: auto;
			margin-right: auto;
			margin-bottom: 50rpx;
			border-radius: 50%;
			border-style: groove;
			-moz-box-shadow:0 0 7px 7px #06c;
			-webkit-box-shadow:0 0 7px 7px #06c;
			box-shadow:0 0 7px 7px #06c;
		}
		.inputname {			//输入框用户名
			width: 50%;
			flex-direction: row;
			display: flex;
			.hintName{			//输入框提示
				width: 90px;
				font-size: 14px;
				flex-direction: row;
				display:flex;
				align-items: center;
			}
			.hintPassword{		//输入框提示	
				width: 90px;
				margin-top: 20px;
				flex-direction: row;
				display: flex;
				align-items: center;
				font-size: 14px;
			}
			.userName{			//用户名
				width: 100%;
				height: 2em;
				border-radius: 3px;
				background-color: #FFFFFF;
				font-size: 16px;
				color: #000000;
				-moz-box-shadow: inset 0 0 10px #CCC;
				-webkit-box-shadow: inset 0 0 10px #CCC;
				box-shadow: inset 0 0 10px #CCC;
			}
			.userPassword{		//密码
				width: 100%;
				height: 2em;
				background-color: #FFFFFF;
				border-radius: 3px;
				margin-top: 20px;
				font-size: 14px;
				color: #000000;
				-moz-box-shadow: inset 0 0 10px #CCC;
				-webkit-box-shadow: inset 0 0 10px #CCC;
				box-shadow: inset 0 0 10px #CCC;
			}
		}
		.forget{				//忘记密码
			font-size: 12px;
			margin-left: 40px;
			margin-top: 20px;
			color: #2B85E4;
		}
		.button-LogReg{			//注册和登录按钮
			width: 50%;
			height: 35px;
			font-size: 16px;
			font-weight: bold;
			margin-top: 60px;
			margin-left: 10rpx;
			margin-right: 10rpx;
		}
		.title {				//页面标题
			display: flex;
			justify-content: center;
			align-items: center;
			margin-top: 200upx;
			text-align: center;
			font-size: 28px;
			font-weight: 500;
			margin-bottom: 80upx;
		}
		input {					//输入框设置
			text-align: left;
			margin-bottom: 10rpx;
			padding-bottom: 6rpx;
		}
		
		// 第三方登录按钮
		.loginAPI-wrap{
			display: flex;
			flex-direction: row;
		}
		.loginAPI_icon{
			width: 32px;
			height: 32px;
			margin: 10px;
		}
	}
	
	.back{
		width: 24px;
		height: 24px;
		left: 15rpx;
		position: absolute;
		top: 45px;
		z-index: 2;
	}
	
	.aboutpassword{
		display: flex;
		flex-direction: row;
		align-items: center;
	}
</style>
