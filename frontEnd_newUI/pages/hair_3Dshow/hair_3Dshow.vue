<template>
	<view>
		<view class="table-header">
			<view v-for="index in 8" :key="index" :class="{'table-header-item':index!==1,'table-header-item-left':index==1}">
				<view class="header-item-wrap">
					<view v-if="index==1" class="monthTag">
						<view style="width: 100%;">2</view>
						<view style="width: 100%;">月</view>
					</view>
					<view v-else :class="{'weekDay':true,'todayTag':index==3}">
						<view>
							周{{getDayOfWeek(index-1)}}
						</view>
						<view>
							{{index-1}}日
						</view>
					</view>
				</view>
			</view>
		</view>
		<view class="table">
			<view v-for="column in 8" :class="{'table-item-wrap':column!==1,'table-item-left-wrap':column==1,'todayTag':column==3}" :key="column">
				<view v-for="row in [1,3,5,7,9]" :key="row" class="courseBlock">
					<view v-if="column!==1">
						<!-- column从2开始，所以-2 -->
						<view v-if="courseWeekAssign[column-2][(row-1)/2]!=-1" @click="courseDetail(courseName[courseWeekAssign[column-2][(row-1)/2]])" :class="{'table-item':true,'table-item-inactive': column==-1}" :style="{'background-color': colorList()[column],'height':windowHeight}">
							{{courseName[courseWeekAssign[column-2][(row-1)/2]]}}
						</view>
						<view v-else :class="{'table-item2':true}" :style="{'background-color': colorList()[18],'height':windowHeight}">
							
						</view>
						<view v-if="row==3||row==7" class="lunchBreak"></view>
					</view>
					<view v-else>
						<view class="table-item-left table-item" :style="[{height: windowHeight}]">
							<view class="time">
								{{row}}
							</view>
							<view>
								|
							</view>
							<view class="time">
								{{row+1}}
							</view>
						</view>
						<view v-if="row==3||row==7" class="lunchBreak"></view>
					</view>
				</view>
			</view>
		</view>
		<!-- 设置一条分割线 -->
		<view :style="{'height':'1px','width':'100%','background-color':'pink'}"></view>
		<view class="header">
			<view class="header-item">
				<image class="refresh-all" @click="refreshORall(1)" src="../../static/refresh.png"></image>
			</view>
			<view class="header-item-week">
				<image class="refresh-all" @click="lastOrnext(1)" src="../../static/left.png"></image>
				<picker :range="week" :value="0" class="header-item">第2周</picker>
				<image class="refresh-all" @click="lastOrnext(2)" src="../../static/right.png"></image>
			</view>
			<view class="header-item">
				<image class="refresh-all" @click="refreshORall(2)" src="../../static/all.png"></image>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				title: '音符课程表',
				
				week:['第1周','第2周','第3周'],
				windowHeight:"105px",			//因为uniapp获取屏幕高度的功能不完善导致测量不准确，所以只能手动确定高度
				
				courseWeekAssign:[[1,2,-1,-1,2],[-1,-1,3,2,-1],[1,-1,2,3,-1],[1,2,-1,3,2],[2,-1,1,-1,3],[2,-1,-1,2,-1],[-1,0,-1,-1,1]],
				courseName:['计算机系统','操作系统','计算机网络','物联网通信'],
			}
		},
		onLoad() {
			return;
			//将当前课表显示到屏幕上
			uni.getStorage({
				key:"courseStorage",
				success(res){
					console.log("获取课表成功");
				},
				fail() {
					console.log("获取课表失败")
				}
			});
			
		},
		onShow() {
			
		},
		//导航栏按钮点击事件
		onNavigationBarButtonTap(button) {
			uni.showToast({
				title:button.text=="主页"?"点击主页":"点击退出",
				icon:"none"
			})
		},
		onPullDownRefresh() {
			//关闭刷新
			uni.stopPullDownRefresh();
		},
		computed: {
			
		},
		methods: {
			//返回颜色
			colorList() {
				return [
					"#00CCFF", //0
					"#8D4BBB", //1
					"#33CC99",
					"#EF7A82", //3
					"#789262", //4
					"#66CCCC", //5
					"#9999FF", //6
					"#6699CC", //7
					"#88ADA6", //8
					"#9D2933", //9
					"#758a99", //10
					"#549688", //11
					"#815476", //12
					"#4b5cc4", //13
					"#DB5A6B", //14
					"#FF00CC", //15
					"#C83C23", //16
					"#44CEF6", //17
					"#FFFFFF",
				]
			},
			//刷新或查看全部课程
			refreshORall(refresh_all){
				uni.showToast({
					title:refresh_all==1?"刷新课表":"查看全部课程",
					icon:"none"
				})
			},
			//切换上下周
			lastOrnext(lORr){
				uni.showToast({
					title:lORr==1?"切换上一周":"切换下一周",
					icon:"none"
				})
			},
			
			//课程细节
			courseDetail(courseName){
				uni.showModal({
					title:courseName,
					content:"教师:老\t唐\n教室:D1234\n周次:1-3,7-9",
					showCancel:false,
					confirmText:"返回课表"
				})
			},
			getDayOfWeek(index) {
				switch (index) {
					case 1:
						return "一"
					case 2:
						return "二"
					case 3:
						return "三"
					case 4:
						return "四"
					case 5:
						return "五"
					case 6:
						return "六"
					case 7:
						return "日"
				}
			}
		},
	}
</script>

<style>
	.header {
		display: flex;
		font-size: 0.8em;
		margin: 20rpx;
		text-align: center;
	}

	.header-item {
		align-self: center;
		margin-left: 10rpx;
		margin-right: 10rpx;
		flex: 1;
	}
	.header-item-week{	
		display: flex;
		flex-direction: row;
	}

	.refresh-all {
		height: 20px;
		width:  20px;	//设置按钮大小
	}

	.table-header {
		display: flex;
		flex-direction: row;
		text-align: center;
		font-size: .7em;
		border: #E4E7ED .1rpx solid;
		padding-top: 10rpx;
		padding-bottom: 10rpx;
	}

	.table {
		display: flex;
		text-align: center;
		background-color: #fdfdfd;
	}

	.table-header-item {
		flex: 1;
	}

	.table-item-wrap {
		flex: 1;
		background-color: #ffffff;
	}

	.table-item-left-wrap {
		background-color: #FFF4DD;
		width: 30px;
		height: 100%;
	}

	.table-header-item-left {
		/* flex: 1; */
		width: 30px;
	}

	.table-item {
		margin-top: 8rpx;
		margin-bottom: 8rpx;
		margin-left: 6rpx;
		margin-right: 6rpx;
		border-radius: 8rpx;
		box-shadow: 1px 1px 2px .1px #b6b6b6;
		text-align: center;
		align-self: center;
		align-items: center;
		justify-content: center;
		display: flex;
		word-break: break-all;
		overflow: hidden;
		font-size: .7em;
		/* padding: 1rpx; */
		color: #ffe8dd;
		font-weight: bold;
		box-sizing: border-box;
	}
	.table-item2 {
		margin-top: 8rpx;
		margin-bottom: 8rpx;
		margin-left: 6rpx;
		margin-right: 6rpx;
		background-color: #ffffff;
		border-radius: 8rpx;
		text-align: center;
		align-self: center;
		align-items: center;
		justify-content: center;
		display: flex;
		word-break: break-all;
		overflow: hidden;
		font-size: .7em;
		padding: 1rpx;
		color: #ffffff;
		box-sizing: border-box;
	}
	.monthTag{
		width: 100%;
		height: 100%;
		font-weight: bold;
	}
	.table-item-left {
		box-sizing: border-box;
		color: #040038;
		border-radius: 5rpx;
		width: 30px;
		position: relative;
		font-size: .8em;
		padding: 1rpx;
		box-shadow: 0 0px 0px #ccc;
		display: flex;
		flex-direction: column;
	}
	.lunchBreak{
		height: 10px;
	}

	.time {
		text-align: center;
		align-self: center;
		margin: 5rpx;
	}

	.weekDay {
		background-color: #ffffff;
		border-radius: 10rpx;
		margin: 6rpx;
	}
	.todayTag{
		border-radius: 3px;
		box-shadow: 0px 0px 2px 3px #d4d6ff inset;
	}
	.courseBlock{
		
	}
</style>
