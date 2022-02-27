<template>
	<view class="content">
		<view class="headPhoto-nick-wrap">
			<image class="head-photo" :src="head_icon" @click="changeHead_icon"></image>
			<view class="nick-text-wrap">
				<text class="nick" @click="changeNick">{{nick}}</text>
				<view class="account-wrap">
					<text class="id">账户：{{account}}</text>
					<view class="identify-wrap">
						<image class="identify-icon" src="../../../../../static/identify_icon.png"></image>
						<text class="identify">{{identify}}</text>
					</view>
				</view>
			</view>
		</view>
		
		<view class="item-wrap" v-for="i in 4" :key="i">
			<view class="item" @click="clickContent(i)">
				<view class="icon-wrap">
					<image class="arrow-icon icon-item" src="../../../../../static/bank4.png"></image>
				</view>
				<view class="text-wrap">
					<text class="item-text">{{content[i-1]}}</text>
					<view class="right-icon-wrap">
						<text class="detail-text">{{tips[i-1]}}</text>
					</view>
				</view>
				<view class="icon-wrap">
					<!-- <image v-if="i==1" class="head-photo" src="../../../../static/head_man1.png"></image> -->
					<image class="arrow-icon" src="../../../../../static/arrow.png"></image>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				nick: "兔子一号",
				account: 123456,
				
				content: ['个性签名','编辑个人资料','动态','我的名片'],
				tips: ['介绍一下你自己','','',''],
				head_icon: "../../../../../static/head_man1.png",
				
				identify: "已认证"
			}
		},
		methods: {
			clickContent(index){
				this.$u.toast("点击了"+this.content[index-1])
				if(index==1){
					uni.navigateTo({
						url: './mySignature/mySignature',
					})
				}
				
				else if(index==2){
					uni.navigateTo({
						url: 'editMyData/editMyData'
					})
				}
				else if(index==3){
					uni.navigateTo({
						url: 'myDynamic/myDynamic'
					})
					return;
				}
				else if(index==4){
					uni.navigateTo({
						url: 'editMyData/myCode/myCode'
					})
					return;
				}
			},
			//换头像
			changeHead_icon(){
				uni.navigateTo({
					url: "changeHead_icon/changeHead_icon"
				})
			},
			
			//昵称
			changeNick(){
				uni.navigateTo({
					url: 'editMyData/myNick/myNick'
				})
				return;
			}
		}
	}
</script>
	
<style>
	.content{
		width: 100%;
		height: 100%;
	}
	.headPhoto-nick-wrap{
		width: 100%;
		height: 80px;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: left;
		border-style: solid;
		border-width: 1px;
		border-color: #999791;
	}
	.head-photo{
		width: 72px;
		height: 72px;
		border-radius: 10%;
		margin-left: 10rpx;
	}
	.nick-text-wrap{
		margin-left: 20rpx;
		display: flex;
		flex-direction: column;
	}
	.nick{
		font-size: 20px;
		font-weight: bold;
	}
	
	//账户
	.account-wrap{
		margin-top: 10px;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
	}
	.id{
		font-size: 14px;
		color: #606266;
	}
	
	//认证
	.identify-wrap{
		border-style: solid;
		border-width: 1px;
		border-color: #0000FF;
		border-radius: 10%;
		margin-left: 8rpx;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
	}
	.identify-icon{
		width: 14px;
		height: 14px;
	}
	.identify{
		font-size: 12px;
		color: #0000FF;
	}
	
	//item
	.item-wrap{
		width: 100%;
		height: 40px;
		/* border-style: groove; */
		border-style: solid;
		border-width: 1px;
		border-color: #999791;
	}
	.item{
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
	}
	.text-wrap{
		flex: 5;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
	}
	.item-text{
		font-size: 16px;
		/* text-align: left; */
		padding-left: 5rpx;
		/* flex: 1; */
	}
	.right-icon-wrap{
		/* flex: 2; */
		display: flex;
		flex-direction: row;
	}
	.detail-text{
		font-size: 14px;
		padding-right: 4rpx;
		color: #968f8d;
	}
	.icon-wrap{
		flex: 1;
		height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.arrow-icon{
		width: 16px;
		height: 16px;
	}
	.icon-item{
		width: 24px;
		height: 24px;
	}
</style>
