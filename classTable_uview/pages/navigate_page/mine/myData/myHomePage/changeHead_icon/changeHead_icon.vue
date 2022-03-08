<template>
	<view class="content">
		<image class="bgimg" src="../../../../../../static/bgSky.png"></image>
		<!-- <image class="img" v-for="(item,index) in imgArray" :src="item" :key="index"></image> -->
		<view class="img-wrap">
			<image class="img" :src="imgArray[0]"></image>
		</view>
		<view class="button-wrap">
			<button class="openCamera" @click="openCamera">打开相机</button>
			<button class="openAlbum" @click="openAlbum">打开相册</button>
			<button class="OK" @click="uploadImg">确认</button>
		</view>
	</view>
</template>

<script>
	export default { 
		data() {
			return {
				imgArray:["../../../../../../static/person.png"]
			}
		},
		onLoad() {
			
		},
		onNavigationBarButtonTap(button) {
			
		},
		methods: {
			//上传图片按钮
			uploadImg(){
				this.$u.toast("点击了上传");
			},
			
			openAlbum(){
				//打开相册
				let that = this;
				uni.chooseImage({
					count: 1,
					success(res) {
						if(res.tempFilePaths.length != 0){
							that.imgArray = res.tempFilePaths;
						}
					}
				});
			},
			
			openCamera(){
				//打开相机，如果没有摄像头的自动打开相册
				var _this=this;
				uni.chooseImage({
				  	count: 1,
				    sizeType: ['original', 'compressed'],
				    sourceType: ['camera'], //这要注意，camera掉拍照，album是打开手机相册
				    success: (res)=> {
						const tempFilePaths = res.tempFilePaths;
						if(tempFilePaths.length != 0){
							_this.imgArray=tempFilePaths;
						}
				    }
				});
			}
		}
	}
</script>

<style>
	.content{
		width: 100%;
		height: 100%;
	}
		
	//图片
	.img-wrap{
		display: flex;
		flex-direction: column;
		align-items: center;
		padding-top: 10px;
	}
	.img{
		border-radius: 10px;
		border-style: groove;
		/* width: 72px;
		height: 72px; */
		width: 80%;
		/* height: 80%; */
	}
	//背景图片
	.bgimg{
		width: 100%;
		height: 100%;
		position: fixed;
		z-index: -1;
	}
	
	//按钮
	.button-wrap{
		width: 100%;
		display: flex;
		flex-direction: column;
		font-size: 16px;
		margin-top: 10rpx;
	}
	.openAlbum{
		width: 100%;
		height: 2em;
		margin-top: 5rpx;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.openCamera{
		width: 100%;
		height: 2em;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.OK{
		width: 100%;
		height: 2em;
		margin-top: 5rpx;
		display: flex;
		align-items: center;
		justify-content: center;
	}
</style>