<template>
	<view class="content">
		<view class="item-wrap" v-for="i in 10" :key="i">
			<view class="item" @click="clickContent(i)">
				<view class="icon-wrap">
					<image class="arrow-icon" src="../../../../../../static/bank4.png"></image>
				</view>
				<view class="text-wrap">
					<text class="item-text">{{content[i-1]}}</text>
					<view class="right-icon-wrap">
						<text v-if="i!=5" class="detail-text">{{tips[i-1]}}</text>
						<text v-else class="detail-text">{{myGender}}</text>
						<image v-if="i==1" class="head-photo" src="../../../../../../static/head_man1.png"></image>
						<image v-if="i==3" class="head-photo" src="../../../../../../static/QRcode.png"></image>
					</view>
				</view>
				<view class="icon-wrap">
					<!-- <image v-if="i==1" class="head-photo" src="../../../../static/head_man1.png"></image> -->
					<image v-if="i!=2&&i!=8" class="arrow-icon" src="../../../../../../static/arrow.png"></image>
					<switch v-if="i==8" class="showAge" @change="showAge"></switch>
				</view>
			</view>
		</view>
		<uni-popup ref="popup" type="bottom" :animation="false" :maskClick="true" @change="change">
			<view v-for="i in 2" :key="i" class="popup-wrap" @click="clickItem(i)">
				<text class="pop-text">{{gender[i-1]}}</text>
			</view>
		</uni-popup>
		
		<!-- 年龄 -->
		<uni-popup ref="popup-age" type="bottom" :animation="false" :maskClick="true">
			<view class="age-wrap" scroll-y>
				<view v-for="i in 100" :key="i" class="popup-wrap" @click="clickAgeItem(i)">
					<text class="pop-text">{{i}}</text>
				</view>
			</view>
		</uni-popup>
	</view>
</template>

<script>
	import uniPopup from "@/components/uni-popup/uni-popup.vue"
	
	export default{
		data(){
			return{
				content: ['头像','我的ID','我的二维码','昵称','性别','个性签名','年龄','是否公开年龄','我的权限','修改密码'],
				tips: ['','123456','','兔子一号','男','未填写','21','','普通用户',''],
				gender: ['男','女'],
				myGender: "男"
			}
		},
		
		//导航栏按钮
		onNavigationBarButtonTap(button) {
			if(button.text=='隐私政策'){
				this.$u.toast("点击了隐私政策")
			}
		},
		
		comments:{
			uniPopup,
		},
		
		methods:{
			clickContent(index){
				if(index==1){
					uni.navigateTo({
						url: "../changeHead_icon/changeHead_icon"
					})
					return;
				}
				else if(index==2){
					this.$u.toast("ID不可修改哦")
					return;
				}
				else if(index==3){
					uni.navigateTo({
						url: 'myCode/myCode'
					})
					return;
				}
				else if(index==4){
					uni.navigateTo({
						url: 'myNick/myNick'
					})
					return;
				}
				else if(index==5){
					this.$refs['popup'].open();
				}
				else if(index==6){
					uni.navigateTo({
						url: '../mySignature/mySignature'
					})
					return;
				}
				else if(index==7){
					this.$refs['popup-age'].open();
					return;
				}
				else if(index==10){
					uni.navigateTo({
						url: "../../../../../login_regist/login/forgetPassword/forgetPassword"
					})
					return;
				}
				// this.$u.toast("点击了"+this.content[index-1])
			},
			// 是否普展现年龄
			showAge(e){
				var _this=this;
				if(e.target.value){
					_this.$u.toast("展示年龄")
				}
				else{
					_this.$u.toast("不展示年龄")
				}
			},
			
			//popup
			change(e){
				
			},
			clickItem(index){
				this.myGender=this.gender[index-1];
				this.$refs['popup'].close();
			},
			clickAgeItem(index){
				// this.myGender=this.gender[index-1];
				this.$refs['popup-age'].close();
			}
		}
	} 
</script>

<style>
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
	.showAge{
		/* 更换大小 */
		transform: scale(0.7);
	}
	
	//弹出层
	.age-wrap{
		height: 90px;
	}
	
	.popup-wrap{
		background-color: #FFFFFF;
		font-size: 16px;
		/* width: 100%; */
	}
	.pop-text{
		display: flex;
		align-items: center;
		justify-content: center;
		border-style: none none solid none;
		border-width: 1px;
		height: 2em;
		margin-top: 5rpx;
	}
</style>