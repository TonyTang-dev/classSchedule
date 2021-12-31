<template>
	<view>
		<view class="swiperContent">
			<view class="page-section-spacing">
				<swiper class="swiper" :indicator-dots="indicatorDots" :autoplay="autoplay" :interval="interval" :duration="duration">
					<swiper-item>
						<image class="swiper-item" @click="selectPoster" src="../../../static/campus.png"></image>
					</swiper-item>
					<swiper-item>
						<image class="swiper-item" @click="selectPoster" src="../../../static/campus4.jpg"></image>
					</swiper-item>
				</swiper>
			</view>
		</view>
		<view class="fillCourse">
			<view class="inputCourseDetail">
				<text class="tipsText">填写课程及课程安排</text>
			</view>
			<view class="inputCourseDetail">
				<textarea class="courseList" :value="courseList" :placeholder="courseAssign"></textarea>
			</view>
			<view class="save-refresh">
				<view class="button-submit" @click="save_refresh">
					<icon type="success"></icon>
					<text class="saveText">保存并刷新</text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				indicatorDots: true,
				autoplay: true,
				interval: 5000,
				duration: 500,
				courseList:'',
				courseAssign:'请输入课程及课程安排(星期+时间)如:\n\t高等数学=1-2 3-1 5-1；\n'+
				'“高等数学”为课程名称，“=”为分隔符;\n“1-2”表示星期一的第二大节即第三四小节课，“3-1”'+
				'则表示星期三的第一大节;\n课程之间以汉语分号分隔，星期之间以空格分隔',
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
					title:"填写课程安排哦",
					icon:"none"
				})
			},
			
			save_refresh(){
				
				//返回课表页
				uni.switchTab({
					url:'../../timeTable/timeTable'
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
	
	//课程安排填写
	.fillCourse{
		margin: 5px;
		padding: 5px;
		border-radius: 3px;
		box-shadow: 0px 0px 2px 2px #0000FF;
	}
	.inputCourseDetail{
		font-size: 16px;
		display: flex;
		flex-direction: row;
		justify-content: center;
	}
	.tipsText{
		margin-top: 10px;
	}
	.courseList{
		width: 80%;
		height: 200rpx;
		font-size: .7em;
		border-radius: 3px;
		padding: 10px;
		margin-top: 20px;
		box-shadow: 0px 0px 0px 3px #ffedce;
	}
	.save-refresh{
		margin-top: 30px;
		display: flex;
		flex-direction: row;
		justify-content: center;
	}
	.button-submit{
		width: auto;
		height: auto;
		padding: 5rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
		border-radius: 5px;
		box-shadow: 0px 0px 1px 2px #ff5500;
	}
	.saveText{
		font-size: .7em;
	}
</style>
