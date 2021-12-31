<template>
    <view>
		<view class="bgContent">
			<view class="myPhoto">
				<image class="header-photo" @click="changeH_N(1)" mode="aspectFit" src="../../static/header-cabbit.png"></image>
				<text class="userName" @click="changeH_N(2)">兔子1号</text>
			</view>
			<image class="bgPhoto" @click="changeBgImage" mode="aspectFill" src="../../static/campus.png"></image>
		</view>
		<view class="APIset">
			<view class="APIRow">
				<view v-for="i in [0,1]" :key='i' class="temp-wrap">
					<view class="button-icon-temp">
						<view class="button-icon" @click="clickAPI(i)">
							<image class="button" :src="icon[i]"></image>
							<text class="APIname">{{APIname[i]}}</text>
						</view>
					</view>
				</view>
			</view>
		</view>
		
		<!-- 注意事项等 -->
		<view class="appDetail">
			<view class="detailButton" v-for="i in [0,1,2]" :key="i" @click="clickDetail(i)">
				<image class="buttonIcon" :src="buttonIcon[i]"></image>
				<text class="buttonText">{{detailButton[i]}}</text>
			</view>
		</view>
		
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
				icon: ['../../static/add.png', '../../static/personal.png'],
				APIname:['添加课程','我的主页'],
				
				//细节按钮
				buttonIcon:['../../static/myData.png','../../static/introduction.png','../../static/system.png'],
				detailButton:['我的资料','使用教程','系统信息'],
			}
		},
		//导航栏按钮点击事件
		onNavigationBarButtonTap(button) {
			uni.showToast({
				title:button.text=="主页"?"点击主页":"点击退出",
				icon:"none"
			})
		},
		methods: {
			//更换头像或昵称
			changeH_N(index){
				uni.showToast({
					title:index==1?"修改头像":"修改昵称",
					icon:"none"
				})
			},
			//更换背景图
			changeBgImage(){
				uni.showToast({
					title:"更换背景图",
					icon:"none"
				})
			},
			//点击API
			clickAPI(i){
				if(i==0){
					uni.navigateTo({
						url:'addCourse/addCourse',
					});
					return;
				}
				else{
					uni.navigateTo({
						url:'myHomepage/myHomepage',
					});
					return;
				}
			},
			//点击细节按钮
			clickDetail(index){
				if(index==0){
					uni.navigateTo({
						url:'myHomepage/myHomepage',
					});
					return;
				}
				else if(index==1){
					uni.navigateTo({
						url:'usingInstruction/usingInstruction',
					});
					return;
				}
				else{
					uni.navigateTo({
						url:'version/version',
					});
					return;
				}
			},
		}
	}
</script>

<style>
	.bgContent{
		background-color: #f3f2f0;
		display: flex;
		height: 150px;
		overflow: hidden;
		flex-direction: row;
		justify-content: center;
		border-radius: 5px;
	}
	.myPhoto{
		display: flex;
		flex-direction: column;
		justify-content: flex-end;
	}
	.bgPhoto{
		filter: blur(5rpx) brightness(70%);//模糊半径和变暗度
	}
	.header-photo{
		margin-left: 20px;
		width: 50px;
		height: 50px;
		border-radius: 50%;
		position: absolute;
		z-index: 2;
		box-shadow: 0px 0px 2px 2px #0000ff;
	}
	.userName{
		position: absolute;
		z-index: 2;
		color: #FFFFFF;
		font-size: 16px;
		margin-left: 80px;
	}
	
	/* API按钮 */
	.APIset{
		margin-top: 70rpx;
		/* height: 200rpx; //因为我需要控件自适应，所以就不固定高度了，空间大小通过子控件的css来设定*/
		box-shadow: 0px 0px 0px 2px #f0fff2;
	}
	.APIRow{
		height: 100rpx;
		/* flex: 1; */
		margin-top: 20px;
		display: flex;
		flex-direction: row;
		justify-content: center;
	}
	.temp-wrap{
		flex: 1;
		display: flex;
		flex-direction: column;
	}
	.button-icon-temp{
		display: flex;
		flex-direction: row;
		justify-content: center;
	}
	.button-icon{
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.button{
		width: 32px;
		height: 32px;
	}
	.APIname{
		font-size: .7em;
	}
	
	/* detail按钮 */
	.appDetail{
		font-size: 16px;
		margin-top: 20px;
	}
	.buttonIcon{
		width: 20px;
		height: 20px;
	}
	.buttonText{
		margin-left: 10px;
	}
	.detailButton{
		box-shadow: 0px 0px 0px 2px #fffced;
		margin-top: 10px;
		padding-left: 10px;
		display: flex;
		flex-direction: row;
		align-items: center;
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
