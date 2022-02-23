<template>
    <view>
		<view class="swiperContent">
			<view class="page-section-spacing">
				<swiper class="swiper" :indicator-dots="indicatorDots" :autoplay="autoplay" :interval="interval" :duration="duration">
					<swiper-item>
						<image class="swiper-item" @click="selectPoster" src="../../static/campus.png"></image>
					</swiper-item>
					<swiper-item>
						<image class="swiper-item" @click="selectPoster" src="../../static/campus4.jpg"></image>
					</swiper-item>
					<swiper-item>
						<image class="swiper-item" @click="selectPoster" src="../../static/campus3.png"></image>
					</swiper-item>
				</swiper>
			</view>
		</view>
		
		<!-- 今日课表预览 -->
		<view class="todaySchedule" @click="switchToSchedule">
			<view class="tips-date">
				<image class="schedule-today" src="../../static/schedule1.png"></image>
				<text class="tips-today">今日课表</text>
				<text class="date-today">第2周 周日</text>				
			</view>
			<view class="course-content">
				<text class="course-detail">操作系统D1234</text>
			</view>
			<view class="tips-date">
				<text class="checkAll">查看完整课表</text>				
			</view>
		</view>
		
		<!-- API按钮接口 -->
		<view class="APIset">
			<view class="APIRow">
				<view v-for="i in [0,1,2]" :key='i' class="temp-wrap">
					<view class="button-icon-temp">
						<view class="button-icon" @click="clickAPI(i)">
							<image class="button" :src="icon[i]"></image>
							<text class="APIname">{{APIname[i]}}</text>
						</view>
					</view>
				</view>
			</view>
			<view class="APIRow">
				<view v-for="j in [3,4,5]" :key='j' class="temp-wrap">
					<view class="button-icon-temp">
						<view class="button-icon" @click="clickAPI(j)">
							<image class="button" :src="icon[j]"></image>
							<text class="APIname">{{APIname[j]}}</text>
						</view>
					</view>
				</view>
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
				icon: ['../../static/schedule1.png', '../../static/newsAPI.png', '../../static/map.png',
					'../../static/memory.png','../../static/english.png','../../static/settingsAPI.png'],
				APIname:['课程表','校园资讯','校园地图','备忘录','英语专栏','系统设置'],
				indicatorDots: true,
				autoplay: true,
				interval: 5000,
				duration: 500
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
			//轮播图点击事件
			selectPoster(){
				uni.showToast({
					title:"积极乐观哦",
					icon:"none"
				})
			},
			//API按钮点击事件
			clickAPI(func){
				switch(func){
					case 0:
						uni.switchTab({
							url:"../timeTable/timeTable",
						});
						break;
					case 1:
						uni.navigateTo({
							url:'campusNews/campusNews',
						});
						break;
					case 2:
						uni.navigateTo({
							url:'map/map',
						});
						break;
					case 3:
						uni.navigateTo({
							url:'memorandum/memorandum',
						});
						break;
					case 4:
						uni.navigateTo({
							url:'englishLearn/englishLearn',
						});
						break;
					case 5:
						uni.switchTab({
							url:'../settings/settings',
						});
						break;
				}
				
			},
			//切换到课程表
			switchToSchedule(){
				uni.switchTab({
					url:'../timeTable/timeTable',
				})
			},
		}
	}
</script>

<style>
	.swiperContent{
		background-color: #f3f2f0;
		padding-bottom: 10px;
		display: flex;
		flex-direction: row;
		justify-content: center;
	}
	.page-section-spacing{	//不能直接对swiper的父亲组件进行对齐方式更改,会出错
		width: 80%;
		margin-top: 10px;
	}
	.swiper-item{
		background-color: #fff1cd;
		border-radius: 5px;
		width: 100%;
		height: 100%;
		text-align: center;
	}
	
	/* 今日课程 */
	.todaySchedule{
		margin-top: 10rpx;
		height: 150rpx;
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
		font-size: .7em;
		display: flex;
		flex-direction: row;
		padding-left: 10px;
	}
	.date-today{
		flex: 1;
		text-align: right;
		padding-right: 10px;
	}
	.tips-today{
		flex: 1;
	}
	.checkAll{
		flex: 1;
		text-align: center;
		margin-top: 3rpx;
		color: #b1b1b1;
	}
	
	.course-content{
		flex: 3;
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
		font-size: 16px;
		font-weight: bold;
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
