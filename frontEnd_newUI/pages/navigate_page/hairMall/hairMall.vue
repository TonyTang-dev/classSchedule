<template>
	<view>
		<view class="swiperContent">
			<view class="page-section-spacing">
				<swiper class="swiper" :indicator-dots="indicatorDots" :autoplay="autoplay" :interval="interval" :duration="duration">
					<swiper-item>
						<image class="swiper-item" @click="selectPoster" src="../../../static/banner1.png"></image>
					</swiper-item>
					<swiper-item>
						<image class="swiper-item" @click="selectPoster" src="../../../static/banner2.png"></image>
					</swiper-item>
				</swiper>
			</view>
		</view>
		
		<view v-for="i in 10" :key='i' style="display: flex; flex-direction: row; margin-top:10px;">
			<view class="recommand">
				<image class="recommand_img" @click="clickPost" :src="recommandHair[i%4]"></image>
				<view class="tips-date">
					<text class="userCount">120人使用</text>
					<text class="clickTry" @click="clickTry">点击试戴</text>				
				</view>
			</view>
			<view class="recommand">
				<image class="recommand_img" @click="clickPost" :src="recommandHair[(i+2)%4]"></image>
				<view class="tips-date">
					<text class="userCount">12人使用</text>
					<text class="clickTry" @click="clickTry">点击试戴</text>				
				</view>
			</view>
		</view>
		
		<!-- 拍照按钮 -->
		<view class="take_wrap">
			<image class="take" @click="takePicture" src="../../../static/takePhoto.png"></image>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				recommandHair:["../../../static/recommand1.png","../../../static/kid.png",
						"../../../static/head_man1.png","../../../static/kid4.png"],
						
				//banner
				indicatorDots: true,
				autoplay: true,
				interval: 5000,
				duration: 500,
			}
		},
		methods: {
			//轮播图点击事件
			selectPoster(){
				uni.showToast({
					title:"点击广告页",
					icon:"none"
				})
			},
			
			//点击推荐
			clickPost(){
				this.$u.toast("点击了推荐");
				uni.navigateTo({
					url: '../Home/hairCommunity/hairDetail/hairDetail'
				});
			},
			clickTry(){
				this.$u.toast("点击了试戴")
			},
			
			//点击拍照按钮
			takePicture(){
				// this.$u.toast("点击拍照按钮")
				uni.navigateTo({
					url:'TakePicture/takePicture',
				})
			}
		}
	}
</script>

<style>
	//banner
	.swiperContent{
		background-color: #f3f2f0;
		padding-bottom: 10px;
		display: flex;
		flex-direction: row;
		justify-content: center;
	}
	.page-section-spacing{	//不能直接对swiper的父亲组件进行对齐方式更改,会出错
		width: 80%;
		margin-top: 10px;
	}
	.swiper-item{
		background-color: #fff1cd;
		border-radius: 5px;
		width: 100%;
		height: 100%;
		text-align: center;
	}
	
	/* 推荐 */
	.recommand{
		width: 50%;
		margin: 10rpx;
		height: 200px;
		border-radius: 10px;
		display: flex;
		flex-direction: column;
		box-shadow: 0px 0px 0px 2px #f0f0f0;
	}
	
	.schedule-today{
		flex-direction: 1;
		width: 20px;
		height: 20px;
	}
	.tips-date{
		font-size: 14px;
		display: flex;
		flex-direction: row;
		padding-left: 10px;
		padding-top: 3px;
	}
	.clickTry{
		flex: 1;
		text-align: right;
		padding-right: 10px;
		border-radius: 5px;
		background-color: #ff5500;
	}
	.userCount{
		flex: 1;
		font-size: 12px;
	}
	.recommand_img{
		width: 100%;
		height: 90%;
		border-radius: 10px;
	}
	
	//打开相册按钮
	.take_wrap{
		width: 100%;
		bottom: 30px;
		border-radius: 50%;
		position: fixed;
		display: flex;
		justify-content: center;
		z-index: 2;
	}
	.take{
		width: 72px;
		height: 72px;
		font-size: 14px;
	}
</style>
