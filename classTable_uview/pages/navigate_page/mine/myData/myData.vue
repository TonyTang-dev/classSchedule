<template>
	<view class="content">
		<view class="item-wrap" v-for="i in 9" :key="i">
			<view class="item" @click="clickContent(i)">
				<view class="icon-wrap">
					<image class="arrow-icon" src="../../../../static/bank4.png"></image>
				</view>
				<view class="text-wrap">
					<text class="item-text">{{content[i-1]}}</text>
					<view class="right-icon-wrap">
						<text class="detail-text">{{tips[i-1]}}</text>
						<image v-if="i==1" class="head-photo" src="../../../../static/head_man1.png"></image>
						<image v-if="i==3" class="head-photo" src="../../../../static/QRcode.png"></image>
					</view>
				</view>
				<view class="icon-wrap">
					<!-- <image v-if="i==1" class="head-photo" src="../../../../static/head_man1.png"></image> -->
					<image v-if="i!=2&&i!=7" class="arrow-icon arrow" src="../../../../static/arrow.png"></image>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				content: ['个人主页','我的账号','我的名片','邀请有礼','我的收藏','修改密码','我的权限','我的生日','设置',],
				tips: ['','123456','','','','','普通用户','01-01','',]
			}
		},
		
		methods:{
			clickContent(index){
				if(index==1){
					uni.navigateTo({
						url: "myHomePage/myHomePage"
					})
					return;
				}
				else if(index==2){
					this.$u.toast("账号不可修改")
					return;
				}
				else if(index==3){
					uni.navigateTo({
						url: 'myHomePage/editMyData/myCode/myCode'
					})
					return;
				}
				
				else if(index==6){
					uni.navigateTo({
						url: '../../../login_regist/login/forgetPassword/forgetPassword'
					})
					return;
				}
				this.$u.toast("点击了"+this.content[index-1])
			}
		}
	} 
</script>

<style>
	//item
	.item-wrap{
		width: 100%;
		height: 50px;
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
		flex: 4;
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
		width: 24px;
		height: 24px;
	}
	.arrow{
		width: 16px;
		height: 16px;
	}
	//头像
	.head-photo{
		width: 24px;
		height: 24px;
		border-radius: 10%;
		/* border-style: groove; */
	}
</style>