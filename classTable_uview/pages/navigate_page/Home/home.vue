<template>
    <view>
		<!-- 左侧菜单栏 -->
		<leftMenu></leftMenu>
		
		<!-- 右上角按钮 -->
		<view class="statusBar">
			<view class="myInfo-wrap">
				<view class="info-wrap">
					<image class="drawer-head-menu" @click="myInfo(1)" src="../../../static/myInfo.png" mode="scaleToFill" />
					<image class="drawer-head-menu" @click="myInfo(2)" src="../../../static/add.png" mode="scaleToFill" />
				</view>
			</view>
		</view>
		
		<view class="u-block" style="marginTop: 70px">
			<u-swiper
				:list="banner"
				:circular="true"
				:autoplay="true"
				previousMargin="30"
				nextMargin="30"
				radius="5"
				bgColor="#ffffff"
				keyName="url"
				:showTitle="true"
				@click="selectPoster">
			</u-swiper>
		</view>
		
		<u-collapse :value="['0']">
			<u-collapse-item name='0' title="今日上新" icon="gift">
				<u-icon name="gift" size="32" slot="icon" color="#ff5500"></u-icon>
				<scroll-view class="today-wrap" scroll-x="true">
					<image class="card-wrap"
							v-for="i in 10" 
							:key="i"
							src="../../../static/new_today.jpeg"
							@click="selectNew(i)"></image>
				</scroll-view>
			</u-collapse-item>
		</u-collapse>
		
		<!-- API按钮接口 -->
		<u-grid
			:border="false" 
			col="4"
			style="marginBottom:20rpx">
			<u-grid-item
					v-for="(item,index) in icon"
					:key="index"
					 @click="clickAPI(index)"
					 style="paddingTop: 20rpx">
				<u-icon
					:customStyle="{paddingTop:20+'rpx'}"
					:name="item"
					:size="32" >
				</u-icon>
				<text class="APIname">{{APIname[index]}}</text>
			</u-grid-item>
		</u-grid>
		<u-line></u-line>
		
		<!-- 版权 -->
		<view class="copyright">
			<text>@Copyright Of 共进小队</text>
		</view>
    </view>
</template>

<script>
	//导入左侧菜单
	import leftMenu from "../../swipeTab/leftMenu.vue";
	
	export default {
		data() {
			return {
				icon: ['../../../static/schedule1.png', '../../../static/newsAPI.png', '../../../static/map.png',
					'../../../static/memory.png','../../../static/english.png','../../../static/settingsAPI.png'
					,'../../../static/schedule1.png','../../../static/settingsAPI.png'],
				APIname:['我的课表','查询课程','找空教室','校车时间','英语备考','校卡余额','一线校园','成绩查询'],
				
				//banner
				banner: [{
						url:"../../../static/campus.png",
						title:"仰天大笑出门去，我辈岂是蓬蒿人"
					},{
						url: "../../../static/campus4.jpg",
						title:"当年少，狂心不已，不醉怎归得"
					},{
						url: "../../../static/campus3.png",
						title:"落日无边江无尽，此身此日更须忙"
					},
					],
				indicatorDots: true,
				autoplay: true,
				interval: 5000,
				duration: 500,
					
				nick: "兔子一号",
				
				barHeight: 30,
			}
		},
		//导航栏按钮点击事件
		onNavigationBarButtonTap(button) {
			// uni.showToast({
			// 	title:button.text=="预约"?"点击预约":"点击退出",
			// 	icon:"none"
			// })
			// if(button.text="退出"){
			// 	uni.redirectTo({
			// 		url:"../../login_regist/login/login",
			// 	})
			// }
		},
		// onNavigationBarSearchInputClicked(e) {
		// 	console.log('点击了搜索框')
		// },

		onLoad(){
			var _this=this
				
			uni.getNetworkType({//获取网络状态
				success(res) {
					if(res.networkType=="none"){
						_this.$u.toast("网络连接失败")
					}
					// else if(res.networkType=="unknown"){
					// 	// _this.$u.toast("您处于未知网络环境中");
					// }
					// else{
					// 	// _this.$u.toast("您处于网络环境中");
					// }
				},
				fail(e) {
					_this.$u.toast("无法获取您的网络状态");
				},
			});
			
			uni.getSystemInfo({
				success(res) {
					_this.barHeight=res.statusBarHeight
				}
			});
		},
		methods: {
			//我的右侧按钮
			myInfo(type){
				if(type==1){
					this.$u.toast("点击了右侧状态按钮");
				}
				else if(type==2){
					this.$u.toast("点击了右侧预约按钮");
				}
			},
			
			//轮播图点击事件
			selectPoster(){
				uni.showToast({
					title:"点击广告页",
					icon:"none"
				})
			},
			//API按钮点击事件
			clickAPI(func){
				var _this=this;
				_this.$u.toast("点击功能"+(_this.APIname[func]));
				// return;	//先直接杀掉函数，后期改
				// if(func!=0 && func != 1 && func!=3 && func!=4 && func != 7){
				// 	return;
				// }
				switch(func){
					case 0:
						// return;
						uni.switchTab({
							url:"../classTable/classTable",
						});
						break;
					case 1:
						// return;
						uni.navigateTo({
							url:'',
						});
						break;
					case 2:
						_this.$u.toast("点击功能"+(func+1));
						return;
						uni.navigateTo({
							url:'',
						});
						break;
					case 3:
						uni.navigateTo({
							url:'',
						});
						break;
					case 4:
						uni.navigateTo({
							url:'englishLearn/englishLearn',
						});
						break;
					case 5:
						_this.$u.toast("点击功能"+(func+1));
						return;
						uni.switchTab({
							url:'',
						});
						break;
					case 6:
					
						break;
					case 7:
						uni.navigateTo({
							url:'',
						});
						break;
				}
				
			},
			
			// 选择新品
			selectNew(index){
				this.$u.toast("选择新品"+index)
			}
		},
		
		//组件注册
		components:{
			leftMenu,
		}
	}
</script>

<style>
	//状态栏
	.statusBar{
		width: 100%;
		height: 70px;
		position: fixed;
		top: 0;
		background-color: #ffffff;
		z-index: 998;
	}
	//右上角按钮
	.myInfo-wrap{
		display: inline-block;
		position: fixed;
		top: 70rpx;
		right: 10rpx;
		/* z-index: 998; */
	}
	.info-wrap{
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
	}
	.drawer-head-menu{
		/* display: inline-block;
		position: fixed; */
		border-radius: 50%;
		/* top: 6px;
		left: 10px; *//* 
		z-index: 999; */ 
		margin-right: 3px;
		width:64rpx;
		height: 64rpx;
	}
	
	/* 推荐 */
	.recommand{
		width: 50%;
		margin: 10rpx;
		height: 200px;
		border-radius: 10px;
		display: flex;
		flex-direction: column;
		box-shadow: 0px 0px 0px 2px #f0f0f0;
	}
	
	.schedule-today{
		flex-direction: 1;
		width: 20px;
		height: 20px;
	}
	.tips-date{
		font-size: 14px;
		display: flex;
		flex-direction: row;
		padding-left: 10px;
		padding-top: 3px;
		z-index: 2;
	}
	.clickTry{
		flex: 1;
		height: 1.5em;
		text-align: center;
		text-align: right;
		padding-right: 10px;
		border-radius: 5px;
		background-color: #ff5500;
	}
	.userCount{
		flex: 1;
		font-size: 12px;
	}
	.recommand_img{
		width: 100%;
		height: 90%;
		border-radius: 10px;
	}
	
	/* 细节按钮 */
	.APIname{
		font-size: 14px;
	}
	
	/* 版权 */
	.copyright{
		font-size: 12px;
		color: #999791;
		display: flex;
		flex-direction: row;
		justify-content: center;
		margin-top: 15px;
	}
	
	/* 今日上新 */
	.today-wrap{
		display: flex;
		flex-direction: row;
		white-space: nowrap;
		margin-left: 10rpx;
		margin-top: 5rpx;
	}
	.card-wrap{
		display: inline-block;
		width: 128rpx;
		height: 128rpx;
		border-radius: 10%;
		margin: 5rpx;
		/* background-color: #FF5500; */
	}
</style>
