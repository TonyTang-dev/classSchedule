<template>
	<view class="content">
		<u-cell-group>
			<u-cell
				v-for="(item,index) in content" :key="index"
			    :title="item"
				:icon="apiIcon[index]"
				:iconStyle="{'color':iconColor[index]}"
			    isLink
				:rightIcon="index==7?'':'arrow-right'"
				size="large"
				:value="tips[index]"
			    :url="detailUrl[index]"
				 @click="clickContent(index)">
				<image v-if="index==0" slot="value" class="head-photo" src="../../../../../../static/head_man1.png"></image>
				<image v-if="index==2" slot="value" class="head-photo" src="../../../../../../static/QRcode.png"></image>
				<switch v-if="index==7" slot="value" class="showAge" @change="showAgeOrNot"></switch>
			</u-cell>
		</u-cell-group>
		
		<!-- <view class="item-wrap" v-for="i in 10" :key="i">
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
				<view class="icon-wrap"> -->
					<!-- <image v-if="i==1" class="head-photo" src="../../../../static/head_man1.png"></image> -->
					<!-- <image v-if="i!=2&&i!=8" class="arrow-icon" src="../../../../../../static/arrow.png"></image>
					<switch v-if="i==8" class="showAge" @change="showAge"></switch>
				</view>
			</view>
		</view> -->
		
		<u-picker :show="showGender" 
			:closeOnClickOverlay="true"
			@close="closeGenderPicker" 
			@cancel="closeGenderPicker" 
			@confirm="selectGender"
			:columns="gender">
		</u-picker>
		
		<u-picker :show="showAge"
			:closeOnClickOverlay="true"
			@close="closeAgePicker" 
			@cancel="closeAgePicker" 
			@confirm="selectAge"
			:columns="Age">
		</u-picker>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				content: ['头像','我的ID','我的二维码','昵称','性别','个性签名','年龄','是否公开年龄','我的权限','修改密码'],
				tips: ['','123456','','兔子一号','男','未填写','21','','普通用户',''],
				
				showGender: false,
				gender: [['男','女']],
				myGender: "男",
				
				showAge: false,
				Age: [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]],
				
				apiIcon: ['info','fingerprint','server-man','chat','star','lock','info-circle','bell','setting','fingerprint'],
				detailUrl: ['../changeHead_icon/changeHead_icon','','myCode/myCode',
					'myNick/myNick','','../mySignature/mySignature',
					'','','','../../../../../login_regist/login/forgetPassword/forgetPassword'],
				iconColor: ['#0000ff','#ff0000','#ffaa00','#ff0000','#ff007f','#5555ff','#ffaa00','#ff0000','#ff007f','#5555ff'],
			}
		},
		
		//导航栏按钮
		onNavigationBarButtonTap(button) {
			if(button.text=='隐私政策'){
				this.$u.toast("点击了隐私政策")
			}
		},
		
		comments:{
			
		},
		
		methods:{
			clickContent(index){
				// if(index==1){
				// 	uni.navigateTo({
				// 		url: "../changeHead_icon/changeHead_icon"
				// 	})
				// 	return;
				// }
				// else if(index==2){
				if(index==1){
					this.$u.toast("ID不可修改哦")
					return;
				}
				else if(index==4){
					// this.$refs['popup'].open();
					this.showGender=true;
				}
				// else if(index==3){
				// 	uni.navigateTo({
				// 		url: 'myCode/myCode'
				// 	})
				// 	return;
				// }
				// else if(index==4){
				// 	uni.navigateTo({
				// 		url: 'myNick/myNick'
				// 	})
				// 	return;
				// }
				
				// else if(index==6){
				// 	uni.navigateTo({
				// 		url: '../mySignature/mySignature'
				// 	})
				// 	return;
				// }
				else if(index==6){
					this.showAge=true;
					return;
				}
				// else if(index==10){
				// 	uni.navigateTo({
				// 		url: "../../../../../login_regist/login/forgetPassword/forgetPassword"
				// 	})
				// 	return;
				// }
				// this.$u.toast("点击了"+this.content[index-1])
			},
			// 是否普展现年龄
			showAgeOrNot(e){
				var _this=this;
				if(e.target.value){
					_this.$u.toast("展示年龄")
				}
				else{
					_this.$u.toast("不展示年龄")
				}
			},
			
			closeGenderPicker(){
				this.showGender=false;
			},
			selectGender(e){
				this.tips[4]=e.value[0];
				this.showGender=false;
			},
			closeAgePicker(){
				this.showAge=false;
			},
			selectAge(e){
				this.tips[6]=e.value[0];
				this.showAge=false;
			},
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
</style>