<template>
	<view class="content">
		<!-- 背景图片 -->
		<image class="bg"></image>
		
		<text class="title">漫画滤镜 卡通特效</text>
		
		<image class="logo" :src="myHeadPhoto" @click="clickFace"></image>
		<!-- 提示语 -->
		<text class="tips">自拍+漫画滤镜=漫画脸</text>
		<button class="make" @click="makeCartoonFace">一键制作漫画特效</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				myHeadPhoto: "../../../../static/head_man2.png",
			}
		},
			
		computed: {		
			
		},
		
		methods: {
			onShow(){
				
			},
			
			onLoad(){
				
			},
			
			//上传自拍
			clickFace(){
				this.$u.toast("点击了自拍");
				
				//打开相册
				let that = this;
				uni.chooseImage({
					count: 1,
					success(res) {
						if(res.tempFilePaths.length != 0){
							that.myHeadPhoto = res.tempFilePaths[0];
						}
					}
				});
			},
			
			//点击制作漫画脸
			makeCartoonFace(){
				this.$u.toast("点击了制作漫画脸")
			}
		},
		
		//注册组件
		components:{
			 
		},
	};
</script>

<style lang="scss" scoped>
	.content {					//父容器
		flex-direction: column;
		display: flex;
		align-items: center;
		align-content: center;
		width: 100%;
		height: 100%;
		
		//背景
		.bg{
			width: 100%;
			height: 100%;
			z-index: -1;
			position: fixed;
			background-image: url("../../../../static/bgSky.png");
		}
		
		.title{
			margin-top: 90px;
			font-size: 20px;
			color: #FFFFFF;
			font-weight: bold;
			text-shadow:2px 2px 4px #ff5500;
		}
		
		.logo {					//头像
			height: 240px;
			width: 240px;
			margin-top: 50px;
			margin-left: auto;
			margin-right: auto;
			margin-bottom: 50rpx;
			border-radius: 5%;
			-moz-box-shadow:0 0 3px 3px #06c;
			-webkit-box-shadow:0 0 3px 3px #06c;
			box-shadow:0 0 3px 3px #06c;
			border-style: groove;//凹槽
		}
		//提示文字
		.tips{
			margin-top: 20upx;
			color: #ffffff;
			text-align: center;
			font-size: 14px;
			border: medium double rgb(0, 85, 255);
			// background-color: #55557f;
			border-radius: 5px;
		}
		
		//点击制作按钮
		.make{
			border-radius: 20px;
			background-color: #ff5500;
			font-size: 16px;
			margin-top: 30px;
			color: #FFFFFF;
		}
	}
</style>
