<template>
	<view class="content">
		<image class="bgimg" src="../../../../static/bgImage.png"></image>
		<!-- <image class="img" v-for="(item,index) in imgArray" :src="item" :key="index"></image> -->
		<view class="img-wrap">
			<image class="img" :src="imgArray[0]"></image>
		</view>
		<view class="upButton-wrap">
			<text class="upTextTips">请选择你的美照后上传哦</text>
		</view>
		<view class="take_wrap">
			<view class="upButton-wrap" @click="uploadImg">
				<image class="upload_icon" src="../../../../static/up.png"></image>
				<text class="upText">上传</text>
			</view>
		</view>
	</view>
</template>

<script>
	export default { 
		data() {
			return {
				imgArray:["../../../../static/person.png"]
			}
		},
		onLoad() {
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
		},
		onNavigationBarButtonTap(button) {
			if(button.text == "相册"){
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
			}
		},
		methods: {
			//上传图片按钮
			uploadImg(){
				this.$u.toast("点击了上传");
			}
		}
	}
</script>

<style>
	.content{
		width: 100%;
		height: 100%;
	}
	//上传图片按钮
	.take_wrap{
		width: 100%;
		bottom: 60px;
		position: fixed;
		display: flex;
		justify-content: center;
		z-index: 2;
	}
	.upButton-wrap{
		display: flex;
		flex-direction: column;
		justify-content: center;
	}
	.upload_icon{
		width: 32px;
		height: 32px; 
		font-size: 14px;
		border-radius: 5px;
		-moz-box-shadow:0 0 3px 3px #06c;
		-webkit-box-shadow:0 0 3px 3px #06c;
		box-shadow:0 0 3px 3px #06c;
	}
	.upText{
		font-size: 14px;
		margin-top: 5px;
		text-align: center;
	}
	//提示语
	.upTextTips{
		font-size: 14px;
		margin-top: 20px;
		text-align: center;
		font-weight: bold;
	}
		
	//图片
	.img-wrap{
		display: flex;
		flex-direction: column;
		align-items: center;
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
</style>