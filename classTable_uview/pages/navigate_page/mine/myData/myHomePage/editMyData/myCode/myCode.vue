<template>
	<view class="content">
		<view class="card-wrap">
			<view class="headPhoto-nick-wrap" @click="myHomePage">
				<view class="left-wrap">
					<image class="head-photo" :src="head_icon" @click="changeHead_icon"></image>
					<view class="nick-text-wrap">
						<text class="nick">{{nick}}</text>
						<view class="account-wrap">
							<text class="id">账户：{{account}}</text>
							<view class="identify-wrap">
								<image class="identify-icon" src="../../../../../../../static/identify_icon.png"></image>
								<text class="identify">{{identify}}</text>
							</view>
						</view>
					</view>
				</view>
				<view class="icon-wrap">
					<image class="arrow-icon" src="../../../../../../../static/arrow.png"></image>
				</view>
			</view>
			<view class="line"></view>
			<view class="code-wrap">
				<text class="tipText">扫描下方二维码获取我的名片</text>
				<image class="code" :src="QRcode"></image>
			</view>
		</view>
		<view class="save-wrap" @click="save_code">
			<view class="saveIcon-wrap">
				<image class="save" src="../../../../../../../static/add.png"></image>
			</view>
			<text class="save-text">保存到相册</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				nick: "兔子一号",
				account: 123456,
				head_icon: "../../../../../../../static/head_man1.png",
				
				identify: "已认证",
				QRcode: "../../../../../../../static/QR_test.png"
			}
		},
		methods: {
			changeHead_icon(){
				uni.navigateTo({
					url: "changeHead_icon/changeHead_icon"
				})
			},
			
			//跳转到我的主页
			myHomePage(){
				uni.navigateTo({
					url: '../../myHomePage'
				})
			},
			
			//保存二维码
			save_code(){
				this.$u.toast("点击了保存到相册")
			}
		}
	}
</script>

<style>
	page{
		background-color: #DCDCDC;
	}
	.content{
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.card-wrap{
		width: 95%;
		background-color: #FFFFFF;
		border-radius: 5%;
		margin-top: 10rpx;
		padding: 10rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.line{
		width: 90%;
		height: 1px;
		background-color: #6c6c6c;
		margin-top: 10rpx;
		margin-bottom: 10rpx;
	}
	.headPhoto-nick-wrap{
		width: 100%;
		height: 80px;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: left;
		/* border-style: solid;
		border-width: 1px;
		border-color: #999791; */
	}
	.left-wrap{
		flex: 5;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: left;
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
	
	//二维码部分
	.code-wrap{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.tipText{
		font-size: 16px;
		color: #968F8D;
	}
	.code{
		width: 512rpx;
		height: 512rpx;
		border-style: groove;
		border-radius: 5%;
	}
	//arrow
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
	
	//保存
	.save-wrap{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.saveIcon-wrap{
		background-color: #FFFFFF;
		width: 40px;
		height: 40px;
		margin-top: 30rpx;
		border-radius: 50%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.save{
		width: 32px;
		height: 32px;
	}
	.save-text{
		font-size: 14px;
		color: #968F8D;
	}
</style>
