<template>
	<view class="content" :style="setParam">
		<text class="count">{{now}}/{{sourcePhoto.length}}</text>
		<image class="back" @click="back" src="../../../../../static/back.png"></image>
		
		<view class="swiperContent">
			<view class="page-section-spacing">
				<swiper class="swiper" 
						:indicator-dots="indicatorDots" 
						:autoplay="autoplay" 
						:interval="interval" 
						:duration="duration"
						@change="slidePic">
					<swiper-item class="swiper-item" v-for="i in 5" :key="i">
						<image class="logo" :src="sourcePhoto[i-1]"></image>
						<text class="detailText" scroll-y="true">{{detailText[i-1]}}</text>
					</swiper-item>
				</swiper>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				now: "1",
				sourcePhoto: [
						"../../../../../static/kid.png","../../../../../static/kid2.png",
						"../../../../../static/kid3.png","../../../../../static/kid4.png","../../../../../static/kid.png",
							],
				detailText: ["这是测试文本文本文本笨笨哦不呢吧\nfefdedewedw",
						"这是测试文本文本文本笨笨哦不呢吧\n\raaaaaaaaa",
						"这是测试文本文本文本笨笨哦不呢吧\nbbbbbbbbbbb",
						"这是测试文本文本文本笨笨哦不呢吧\nccccccccccccc",
						"这是测试文本文本文本笨笨哦不呢吧\nddddddddddddd",
							],
				
				// windowHeight: 0,
				setParam: {
					height: "300px",
				},
				
				//banner
				indicatorDots: false,
				autoplay: false,
				interval: 5000,
				duration: 500,
			}
		},
		onLoad() {
			var _this=this;
			
			uni.getSystemInfo({
			    success: function (res) {
			        // console.log(res.windowHeight);
					// _this.windowHeight=res.windowHeight;
					_this.setParam.height=res.screenHeight+"px";
			    }
			});
		},
		
		methods: {
			//滑动图片
			slidePic(e){
				this.now=e.detail.current+1;
			},
						
			// back
			back(){
				uni.navigateBack({
					delta:1,
				});
			}
		}
	}
</script>
	
<style>
	.content{
		width: 100%;
		height: 800px;
		display: flex;
		flex-direction: column;
		/* justify-content: center; */
		align-items: center;
		background-color: #000000;
	}
	
	//计数
	.count{
		/* margin-top: 70px; */
		font-size: 16px;
		color: #FFFFFF;
		right: 20px;
		position: fixed;
		top: 70px;
	}
	.back{
		width: 24px;
		height: 24px;
		left: 20px;
		position: fixed;
		top: 70px;
		z-index: 2;
	}
	
	//banner
	.swiperContent{
		margin-top: 70px;
		width: 100%;
		height: 100%;
		/* background-color: #f3f2f0; */
		padding-bottom: 10px;
		display: flex;
		flex-direction: row;
		justify-content: center;
	}
	.page-section-spacing{	//不能直接对swiper的父亲组件进行对齐方式更改,会出错
		width: 100%;
		height: 100%;
		margin-top: 10px;
	}
	.swiper{
		width: 100%;
		height: 100%;
	}
	.swiper-item{
		/* background-color: #fff1cd; */
		margin-top: 40px;
		border-radius: 5px;
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
	} 
	
	
	.logo {					//头像
		height: 60%;
		width: 95%;
		/* margin-top: 100px; */
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
		border-radius: 5%;
		-moz-box-shadow:0 0 3px 3px #06c;
		-webkit-box-shadow:0 0 3px 3px #06c;
		box-shadow:0 0 3px 3px #06c;
		border-style: groove;//凹槽
	}
	.detailText{
		width: 95%;
		color: #FFFFFF;
		font-size: 15px;
		text-indent: 2em;
		text-align: left;
		padding: 10px;
		/* border-style: groove; */
	}
</style>
