<template> 
	<view class="content"> <!-- :style="{height:heightC - 50  + 'px'}"> -->
		<!-- 背景图片 -->
		<image class="bgimg"></image>
		<!-- 聊天 -->
		<view v-for="(item,idx) in chatList" :key="idx" :class="item.isself?'chatself':'chatother'">
			<image v-if="item.isself" src="../../../../static/mine2.png"
				style="width: 80rpx;height: 80rpx;margin-left: 20rpx; borderRadius: 50%; backgroundColor: #FFFFFF;"></image>
			<image v-else src="../../../../static/mine1.png"
				style="width: 80rpx;height: 80rpx;margin-right: 20rpx; borderRadius: 50%; backgroundColor: #FFFFFF;"></image>
			<view :class="item.isself?'chatbgvS':'chatbgvO'">
				<text style="width: 100%; height: 100%;word-break: break-all;">{{item.msg}}</text>
			</view>
		</view>
		<!-- input -->
		<view class="chatinput">
			<image src="../../../../static/tab_home_s.png" 
				style="width: 80rpx;height: 80rpx;margin: 0rpx 20rpx; borderRadius: 10rpx; backgroundColor: #FFFFFF;"></image>
			<!-- <input class="inputtext" v-model="sendContent" type="text" placeholder="输入要说的内容" /> -->
			<textarea class="inputtext" v-model="sendContent" type="text" placeholder="输入要说的内容" />
			<u-button @click="send" style="width: 15%; height: 60%;" text="发送"></u-button>
		</view>
	</view>
</template>

<script>
	export default {

		data() {
			return {
				heightC: 0,
				sendContent: '',
				chatList: [{
						isself: true,
						msg: '你好'
					},
					{
						isself: false,
						msg: '尊敬的用户：\n请问有什么可以帮到您？'
					},
					{
						isself: true,
						msg: '怎么上传照片？'
					},
					{
						isself: false,
						msg: '到主页点击上传照片即可哦！'
					},
					{
						isself: true,
						msg: '哦哦，好的，谢谢！'
					},
					{
						isself: false,
						msg: '不可气，有什么问题可继续联系我们哦！'
					}
				]
			};
		},
		onLoad() {
			this.heightC = uni.getSystemInfoSync().windowHeight - uni.getSystemInfoSync().statusBarHeight;
		},
		methods: {
			// 发送
			send(){
				if(this.sendContent==""){
					return;
				}
				else{
					var item={
						isself: true,
						msg: this.sendContent
					}
					this.chatList.push(item);
					this.sendContent='';
				}
			}
		}
	}
</script>

<style lang="less">
	/* 背景图片 */
	.bgimg{
		background-color: #0F0F27;
		z-index: -1;
		width: 100%;
		height: 100%;
		position: fixed;
		/* // filter: blur(3rpx) brightness(70%);//模糊半径和变暗度 */
	}
	.content {
		width: 100%;
		overflow: scroll;
		padding-bottom: 50px;

		.chatself {
			display: flex;
			flex-direction: row-reverse;
			width: 90%;
			margin-left: 5%;
			margin-top: 20rpx;
			margin-bottom: 10rpx;
		}

		.chatother {
			display: flex;
			width: 90%;
			margin-left: 5%;
			margin-top: 20rpx;
			margin-bottom: 10rpx;
		}

		.chatbgvS {
			color: #FFFFFF;
			padding: 20rpx 40rpx;
			max-width: calc(90% - 140rpx);
			background-color: #0055ff;
			font-size: 24rpx;
			border-radius: 10px 0px 10px 10px;
			
		}

		.chatbgvO {
			color: #FFFFFF;
			padding: 20rpx 40rpx;
			max-width: calc(90% - 140rpx);
			background-color: #292A3F; 
			font-size: 24rpx;
			border-radius: 0px 10px 10px 10px; 
		}

		.chatinput {
			position: fixed;
			bottom: 0rpx;
			height: 50px;
			width: 100%;
			background-color: #15152D;
			display: flex;
			// justify-content: space-between;
			align-items: center;

			.inputtext {
				width: 70%;//calc(100% - 80rpx - 50rpx - 38rpx);
				height: 70%;
				margin-right: 10rpx;
				color: #FFFFFF;
				font-size: 14px;
				border-style: solid;
				border-width: 1px;
				border-color: #909399;
				border-radius: 5px;
			}
		}
	}
</style>
