<template>
	<view>
		<image class="schoolMap" src="../../../static/mapPhoto.png" @click="clickMap"></image>
		<!-- <map class="schoolMap" scale="5" show-location="true" :longitude="longitude" :latitude="latitude"></map> -->
		
		<button class="tempButton" @click="tempButton">未集成地图，点击返回</button>
		
		<!-- 版权 -->
		<view class="copyright">
			<text>@Copyright Of YingFu</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// longitude:'',
				// latitude:'',
			}
		},
		onLoad() {
			// var _this=this;
			// uni.getLocation({
			// 	type: 'wgs84',
			// 	success(res) {
			// 		_this.longitude=res.longitude;
			// 		_this.latitude=res.latitude;
			// 	}
			// })
		},
		//导航栏按钮点击事件
		onNavigationBarButtonTap(button) {
			uni.showToast({
				title:button.text=="主页"?"点击主页":"点击退出",
				icon:"none"
			})
		},
		methods: {
			clickMap(){
				uni.showToast({
					title:"目前还没有集成地图组件",
					icon:"none"
				})
			},
			tempButton(){
				uni.switchTab({
					url:'../home'
				})
			},
		}
	}
</script>

<style>
	.schoolMap{
		width: 100%;
		height: 300px;
	}
	
	.tempButton{
		width: 60%;
		font-size: 16px;
		color: #ffffff;
		background-color: #ff5500;
		display: flex;
		flex-direction: row;
		justify-content: center;
		margin-top: 15px;
	}
	
	/* 版权 */
	.copyright{
		font-size: .7em;
		color: #999791;
		display: flex;
		flex-direction: row;
		justify-content: center;
		margin-top: 15px;
	}
</style>
