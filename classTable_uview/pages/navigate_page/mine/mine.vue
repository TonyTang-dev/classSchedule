<template>
    <view class="content">
		<!-- 背景图片 -->
		<!-- <image class="bgimg"></image> -->
		
		<!-- 右上角按钮 -->
		<view class="statusBar">
			<view class="myInfo-wrap">
				<view class="info-wrap">
					<image class="drawer-head-menu" @click="myInfo(1)" src="../../../static/myInfo.png" mode="scaleToFill" />
					<image class="drawer-head-menu" @click="myInfo(2)" src="../../../static/add.png" mode="scaleToFill" />
				</view>
			</view>
		</view>
		
		
		<!-- 星球 -->
		<star class="star"></star>
		
		<text class="greet">{{greet}}</text>
		
		<view class="bgContent">
			<view class="myPhoto">
				<view class="wrap-my">
					<view class="flex-wrap">
						<view class="mine-wrap" v-if="isLogin==true">
							<image class="header-photo" @click="changeH_N(1)" mode="aspectFit" src="../../../static/header-cabbit.png"></image>
							<view class="userName" @click="changeH_N(2)">
								<text class="userText">昵称：{{nick}}</text>
								<text class="userText">I D：{{id}}</text>
							</view>
						</view>
						<view class="mine-wrap" v-else @click="selectLogin">
							<image class="header-photo non-login" mode="aspectFit" src="../../../static/mine1.png"></image>
							<view class="userName">
								<text class="userText notLogin">未登录,点我登录哦!</text>
								<!-- <text class="userText">I D：{{id}}</text> -->
							</view>
						</view>
						<text class="minePage" @click="pageMine">个人主页</text>
					</view>
				</view>
			</view>
			<image class="bgPhoto" @click="changeBgImage" mode="bottom" src="../../../static/bg_2.png"></image>
		</view>
		
		<!-- 我的订单之类 -->
		<view class="APIset">
			<view class="APIRow">
				<view v-for="i in [0,1,2]" :key='i' class="temp-wrap line-wrap">
					<view class="button-icon-temp">
						<view class="button-icon" @click="clickFunc(i)">
							<!-- <text class="APIname countNum">{{funcCount[i]}}</text> -->
							<!-- <image class="button" :src="funcIcon[i]"></image> -->
							<text class="APIname">{{mineFunc[i]}}</text>
							<text class="APIname countNum">{{funcCount[i]}}</text>
						</view>
					</view>
				</view>
			</view>
		</view>
		
		<view class="APIset margin-top">
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
		
		<view class="line" style="margin-top:15rpx;width: 100%;height:1px;backgroundColor: #9d9d9d"></view>
		
		<u-cell-group>
			<u-cell
				v-for="(item,index) in detailButton" :key="index"
			    :title="item"
				:icon="iconName[index]"
				:iconStyle="{'color':iconColor[index]}"
			    isLink
				size="large"
				@click="clickDetail(index)"
			></u-cell>
			<!-- :url="detailUrl[index]" -->
		</u-cell-group>
		
		<!-- 注意事项等 -->
		<!-- <view class="appDetail">
			<view class="detailButton" v-for="i in [0,1,2,3,4,5]" :key="i" @click="clickDetail(i)">
				<image class="buttonIcon" :src="buttonIcon[i]"></image>
				<text class="buttonText">{{detailButton[i]}}</text>
			</view>
		</view> -->
		
		<!-- 版权 -->
		<view class="copyright">
			<text>@Copyright Of 共进小队</text>
		</view>
		
		<!-- 弹窗 -->
		<uni-popup ref="popup" class="fatherPop-wrap" type="bottom" :animation="false" :maskClick="true" @change="change">
			<view v-for="i in 2" :key="i" class="popup-wrap" @click="clickItem(i)">
				<text class="pop-text">{{func[i-1]}}</text>
			</view>
		</uni-popup>
    </view>
</template>

<script>
	import uniPopup from "@/components/uni-popup/uni-popup.vue"
	import star from "./star.vue"
	
	export default {
		data() {
			return {
				icon: ['../../../static/add.png', '../../../static/personal.png'],
				APIname:['修改资料','修改密码'],
				
				funcIcon: ['../../../static/add.png', '../../../static/personal.png', '../../../static/hairMall_select.png'],
				mineFunc:['我的账户','我的成绩',"我的课表"],
				funcCount:[8,"-",8],
				
				//细节按钮
				buttonIcon:['../../../static/myData.png','../../../static/introduction.png','../../../static/system.png',
					'../../../static/introduction.png','../../../static/system.png','../../../static/introduction.png'],
				detailButton:['我的资料','分享应用','关于我们','版本信息','我的客服','退出登录'],
				iconName: ['account-fill','share','calendar','bookmark','server-man','info-circle'],
				iconColor: ['#0000ff','#ff0000','#ffaa00','#ff0000','#ff007f','#5555ff'],
				detailUrl:['./myData/myData','shareAPP/shareAPP','aboutUs/aboutUs',
						'myVersion/myVersion','myService/myService',''],
				
				func: ['修改头像','修改昵称'],
				
				nick: "兔子一号",
				id: 123456,
					
				greet: "Hi~,早上好",
				
				isLogin: true
			}
		},
		//导航栏按钮点击事件
		onNavigationBarButtonTap(button) {
			uni.showToast({
				title:button.text=="主页"?"点击主页":"点击退出",
				icon:"none"
			})
		},
		onLoad() {
			var date = new Date().getHours();
			if(date>=0 && date<12){
				this.greet="Hi~,早上好!";
			}
			else if(date>=12 && date<=18){
				this.greet="Hi~,下午好!";
			}
			else{
				this.greet="Hi~,晚上好!";
			}
		},
		
		components:{
			star,
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
			//更换头像或昵称
			changeH_N(index){
				// if(index==1){
					this.$refs['popup'].open();
				// 	// uni.navigateTo({
				// 	// 	url: './myData/myHomePage/changeHead_icon/changeHead_icon'
				// 	// })
				// 	return;
				// }
				// else{
				// 	uni.navigateTo({
				// 		url: 'myData/myHomePage/editMyData/myNick/myNick'
				// 	})
				// 	return;
				// }
			},
			
			// 选择登录
			selectLogin(){
				uni.navigateTo({
					url: '../../login_regist/login/login',
				});
				return;
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
						url:'./myData/myHomePage/myHomePage',
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
						url:'./myData/myData',
					});
					return;
				}
				else if(index==1){
					uni.navigateTo({
						url:'shareAPP/shareAPP',
					});
					return;
				}
				else if(index==2){
					uni.navigateTo({
						url:'aboutUs/aboutUs',
					});
					return;
				}
				else if(index==3){
					uni.navigateTo({
						url: 'myVersion/myVersion'
					});
				}
				else if(index==4){
					uni.navigateTo({
						url:'myService/myService',
					});
					return;
				}
				else{
					if(this.isLogin){
						this.isLogin=false;
					}
					else{
						this.isLogin=true;
					}
				}
			},
			
			// 订单之类
			clickFunc(index){
				this.$u.toast("点击了"+this.mineFunc[index])
			},
			
			// 弹窗
			//popup
			change(e){
				
			},
			clickItem(index){
				if(index==1){
					uni.navigateTo({
						url: './myData/myHomePage/changeHead_icon/changeHead_icon'
					})
				}
				else{
					uni.navigateTo({
						url: 'myData/myHomePage/editMyData/myNick/myNick'
					})
				}
				this.$refs['popup'].close();
			},
			
			// 我的主页
			pageMine(){
				if(this.isLogin==false){
					this.$u.toast("先登录哦!");
					return;
				}
				
				uni.navigateTo({
					url: 'myData/myHomePage/myHomePage',
				});
				return;
			}
		}
	}
</script>

<style>
	/* 背景图片 */
	/* .bgimg{ */
		/* background-image: url("../../../static/bgSky.png"); */
		/* z-index: -1; */
		/* position: fixed; */
	/* } */
	
	//状态栏
	.statusBar{
		/* width: 100%;
		height: 70px;
		position: fixed;
		top: 0;
		background-color: #ffffff;
		z-index: 998; */
	}
	//右上角按钮
	.myInfo-wrap{
		display: inline-block;
		position: absolute;
		top: 70rpx;
		right: 10rpx;
		z-index: 999;
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
	
	.bgContent{
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
		z-index: 2;
	}
	.bgPhoto{
		width: 100%;
		/* filter: blur(5rpx) brightness(70%);//模糊半径和变暗度 */
	}
	.header-photo{
		margin-left: 20px;
		width: 50px;
		height: 50px;
		border-radius: 50%;
		/* position: absolute; */
		/* z-index: 2; */
		box-shadow: 0px 0px 2px 2px #0000ff;
	}
	.non-login{
		background-color: #FFFFFF;
		box-shadow: 0px 0px 2px 2px #ffffff;
	}
	.mine-wrap{
		display: flex;
		flex-direction: row;
	}
	.wrap-my{
		width: 100%;
		display: flex;
		flex-direction: row;
		position: absolute;
	}
	.flex-wrap{
		width: 100%;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: space-between;
	}
	.minePage{
		border-style: solid none solid solid;
		border-radius: 10rpx 0 0 10rpx;
		border-width: 1px;
		border-color: #ffaaff;
		color: #ffffff;
		font-size: 14px;
	}
	.userName{
		/* position: absolute; */
		/* z-index: 2; */
		color: #000000;
		font-weight: bold;
		font-size: 16px;
		margin-left: 10rpx;
		display: flex;
		flex-direction: column;
	}
	.userText{
		font-size: 14px;
		margin-top: 5px;
	}
	.notLogin{
		color: #FFFFFF;
		height: 40px;
		border-radius: 10rpx;
		/* opacity: 0.5; */
		padding: 5rpx;
		display: flex;
		align-items: center;
		justify-content: center;
		background-color: #55557f;
	}
	
	/* API按钮 */
	.APIset{
		margin-top: 70rpx;
		/* height: 200rpx; //因为我需要控件自适应，所以就不固定高度了，空间大小通过子控件的css来设定*/
		box-shadow: 0px 0px 0px 2px #f0fff2;
	}
	.margin-top{
		margin-top: 0;
	}
	.APIRow{
		height: 120rpx;
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
		z-index: 2;
		/* border-style: groove; */
	}
	.button{
		width: 32px;
		height: 32px;
	}
	.APIname{
		font-size: 14px;
		font-weight: bold;
	}
	
	/* 订单之类数量 */
	.countNum{
		font-size: 20px;
	}
	
	/* detail按钮 */
	.appDetail{
		font-size: 16px;
		margin-top: 20rpx;
	}
	.buttonIcon{
		width: 20px;
		height: 20px;
	}
	.buttonText{
		margin-left: 10px;
	}
	.detailButton{
		height: 70rpx;
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
	
	/* 弹窗 */
	.fatherPop-wrap{
		/* margin-bottom: 70rpx; */
		z-index: 999;
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
	
	/* 星球 */
	.star{
		height: 0;
		background-color: #ffaaff;
		/* position: fixed; */
		z-index: 2;
	}
	
	/* 问候语 */
	.greet{
		font-size: 20px;
		color: #FFFFFF;
		font-weight: bold;
		position: absolute;
		z-index: 2;
		top: 70px;
		left: 20rpx;
	}
</style>
