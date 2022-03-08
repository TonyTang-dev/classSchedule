<template>
	<view class="content-wrap">
		<view class="myInfo-wrap" @click="open">
			<view class="info-wrap">
				<image class="drawer-head-menu" src="../../static/header-cabbit.png" mode="scaleToFill" />
				<text class="nick">兔子一号</text>
			</view>
		</view>
		<view @touchstart="touchStart" @touchend="touchEnd">
			<!-- 遮罩层 -->
			<view class="drawer-mask" :class="{ 'drawer-mask-visible': stateDrawer }" @tap="close()" />
			<!-- 内容列表 -->
			<view class="drawer-content" :class="{ 'drawer-content-visible': stateDrawer}">
				<scroll-view style="width: 100%; height: 100%;" scroll-y="true">
					<!-- <view v-for="item in 30" :key="item" @click="selectItem(item)">可滚动内容 {{ item }}</view> -->
				<!-- </scroll-view> -->
					<view class="content">
						<view class="bgContent">
							<view class="myPhoto">
								<image class="header-photo" @click="changeH_N(1)" mode="aspectFit" src="../../static/header-cabbit.png"></image>
								<view class="userName" @click="changeH_N(2)">
									<text class="userText">昵称：兔子1号</text>
									<text class="userText">I D：123456</text>
								</view>
							</view>
							<image class="bgPhoto" @click="changeBgImage" mode="bottom" src="../../static/bg_2.png"></image>
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
							<view class="detailButton" v-for="i in [0,1,2,3,4]" :key="i" @click="clickDetail(i)">
								<image class="buttonIcon" :src="buttonIcon[i]"></image>
								<text class="buttonText">{{detailButton[i]}}</text>
							</view>
						</view>
						
						<!-- 版权 -->
						<view class="copyright">
							<text>@Copyright Of 3D小组</text>
						</view>
					</view>
				</scroll-view>
			</view>
		</view>
	</view>
	
</template>
 
<script>
	/**
	 * Drawer 抽屉侧滑菜单
	 * @property {Boolean} mask = [true | false] 是否显示遮罩
	 * @property {Boolean} maskClick = [true | false] 点击遮罩是否关闭
	 */
	export default {
		name: 'drawer',
		data() {
			return {
				stateDrawer: false,
				startTime: null,  // 手势滑动时间
				startPosition: 0, // 手势进入时
				endPosition: 0    ,// 手势离开时
				
				icon: ['../../../static/add.png', '../../../static/personal.png'],
				APIname:['修改资料','修改密码'],
				
				//细节按钮
				buttonIcon:['../../../static/myData.png','../../../static/introduction.png','../../../static/system.png',
					'../../../static/introduction.png','../../../static/system.png'],
				detailButton:['我的资料','分享应用','关于我们','版本信息','我的客服'],
			}
		},
		created() {
			
		},
		methods: {
			close() {
				this._changeDrawer('stateDrawer', false)
			},
			//选中选项
			// selectItem(index){
			// 	this.$u.toast("选中了元素"+index);
			// 	this._changeDrawer("stateDrawer",false);
			// },
			open() {
				this._changeDrawer('stateDrawer', true)
			},
			_changeDrawer(param, status) {
				this[param] = status
			},
			// 手势进入时
			touchStart(e) {
				this.startTime = Date.now()
				this.startPosition = e.changedTouches[0].clientX
			},
			// 手势离开时
			touchEnd(e){
				const endTime = Date.now()
				if (endTime - this.startTime > 2000){
					return;
				}
				this.endPosition = e.changedTouches[0].clientX;
				var slideDistance = this.endPosition - this.startPosition; 
				if( slideDistance > 50){
					this.open()
				}
				if(slideDistance < -50){
					this.close()
				}
			},
			
			
			
			//更换头像或昵称
			changeH_N(index){
				if(index==1){
					uni.navigateTo({
						url: '../mine/myData/myHomePage/changeHead_icon/changeHead_icon'
					})
					return;
				}
				else{
					uni.navigateTo({
						url: '../mine/myData/myHomePage/editMyData/myNick/myNick'
					})
					return;
				}
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
				// this.$u.toast("点击了"+this.APIname[i]);
				if(i==0){
					uni.navigateTo({
						url:'../mine/myData/myHomePage/myHomePage',
					});
					return;
				}
				else{
					uni.navigateTo({
						url:'../../login_regist/login/forgetPassword/forgetPassword',
					});
					return;
				}
			},
			//点击细节按钮
			clickDetail(index){
				this.$u.toast("点击了"+this.detailButton[index]);
				if(index==0){
					uni.navigateTo({
						url:'../mine/myData/myData',
					});
					return;
				}
				else if(index==1){
					uni.navigateTo({
						url:'',
					});
					return;
				}
				else{
					uni.navigateTo({
						url:'',
					});
					return;
				}
			}
		}
	}
</script>
 
<style scoped>
	.content-wrap{
		width: 100%;
		height: 100%;
	}
	/* 侧滑菜单 外部按钮 */
	.myInfo-wrap{
		display: flex;
		position: fixed;
		top: 70rpx;
		left: 3px;
		z-index: 999;
		width: 30%;
		overflow: hidden;
	}
	.info-wrap{
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
	}
	.nick{
		margin-left: 5px;
		color: #0000FF;
		font-weight: bold;
		font-size: 14px;
	}
	.drawer-head-menu{
		/* display: inline-block;
		position: fixed; */
		border-radius: 50%;
		/* top: 6px;
		left: 10px; *//* 
		z-index: 999; */
		width:64rpx;
		height: 64rpx;
	}
	/* 侧滑菜单 因为需要手势滑动，所以左侧留边20rpx*/
	.drawer-content {
		display: block;
		position: fixed;
		top: 0;
		left: 0;
		width: 70%;
		bottom: 0;
		z-index: 33;
		background-color: rgba(255, 255, 255, 1);
		/* padding: 20rpx 30rpx; */
		/* padding-right: 30rpx; */
		box-sizing: border-box;
		transform: translateX(calc(-100%));
		transition: transform 0.3s ease;
	}
	.drawer-content-visible {
		z-index: 999;
		transform: translateX(0px);
	}
	/* 侧滑菜单 遮罩层 */
	.drawer-mask {
		display: block;
		position: fixed;
		top: 0;
		left: 0;
		bottom: 0;
		right: 0;
		background-color: rgba(0, 0, 0, 0.4);
		opacity: 0;
		transition: opacity 0.3s;
	}
	.drawer-mask-visible {
		z-index: 999;
		opacity: 1;
	}
	.drawer-content view{
		/* font-size: 16px; */
		line-height: 1.5;
		/* margin-top: 10px; */
		margin-bottom: 10px;
	}
	
	.content{
		width: 100%;
		height: 100%;
	}
	.bgContent{
		width: 100%;
		height: 100%;
		background-color: #f3f2f0;
		display: flex;
		height: 175px;
		/* overflow: hidden; */
		flex-direction: row;
		justify-content: center;
		border-radius: 0px;
	}
	.myPhoto{
		display: flex;
		flex-direction: column;
		justify-content: flex-end;
		margin-bottom: 5px;
	}
	.bgPhoto{
		/* z-index: -1; */
		/* filter: blur(5rpx) brightness(70%);//模糊半径和变暗度 */
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
		display: flex;
		flex-direction: column;
	}
	.userText{
		font-size: 14px;
		margin-top: 5px;
	}
	/* .bgContent{
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
	} */
	
	/* API按钮 */
	.APIset{
		/* margin-top: 5rpx; */
		/* height: 200rpx; //因为我需要控件自适应，所以就不固定高度了，空间大小通过子控件的css来设定*/
		box-shadow: 0px 0px 0px 2px #f0fff2;
	}
	.APIRow{
		height: 100%;
		/* flex: 1; */
		/* margin-top: 5px; */
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
		font-size: 14px;
		font-weight: bold;
		z-index: 1;
	}
	
	/* detail按钮 */
	.appDetail{
		font-size: 16px;
		margin-top: 5px;
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
		margin-top: 5px;
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