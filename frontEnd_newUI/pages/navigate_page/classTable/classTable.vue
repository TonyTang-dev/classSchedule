<template>
	<view class="content" :style="{height: windowHeight+'px'}">
		<view class="header-wrap" :style="{marginTop: barHeight+'px'}">
			<view class="left-text">
				<text class="month-text">{{month}}<br>月</text>
				<view class="text-content" v-for="i in 7" :key="i">
					<text class="week-txt">{{week[i-1]}}</text>
					<text class="date-txt">{{date[i-1]}}日</text>
				</view>
			</view>
		</view>
		<u-line></u-line>
		<!-- 课表 -->
		<view class="table-wrap">
			<view class="time">
				<text class="time-text" v-for="i in 4" :key="i">{{i}}</text>
				<text class="time-text">午</text>
				<text class="time-text" v-for="i in [6,7,8,9,10,11]" :key="i">{{i}}</text>
				<text class="time-text" >~</text>
			</view>
			<view class="class-item" v-for="i in 7" :key="i">
				<view class="class-text" v-for="j in 2" :key="j" :style="{backgroundColor: colorList()[j]}">
					<text class="class-name">{{classList[0].name[0]}}</text>
				</view>
				<view class="class-text-noon">
					<text class="class-name"></text>
				</view>
				<view class="class-text" v-for="k in [3,4]" :key="k" :style="{backgroundColor: colorList()[k]}">
					<text class="class-name"></text>
				</view>
				<view class="class-text-night" :style="{backgroundColor: colorList()[17]}">
					<text class="class-name"></text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				month: 1,
				week: ['周一','周二','周三','周四','周五','周六','周日'],
				date: [12,13,14,15,16,17,18],
				windowHeight: 800,
				barHeight: 30,
				
				classList: [
					{
						name: ["操作系统","计算机网络"],
						classroom: ["D1447","D1212"],
						time: ["3-4","6-7"]
					},
					{
						name: ["Linux系统","计算机网络"],
						classroom: ["D1137","D1212"],
						time: ["1-2","11-13"]
					},
				]
			}
		},
		
		onLoad(){
			var _this=this;
			uni.getSystemInfo({
				success(res){
					_this.windowHeight=res.screenHeight
					_this.barHeight=res.statusBarHeight
				},
				fail(){
					_this.windowHeight=600
					_this.barHeight=30
				}
			})
			
			var date=new Date();
			this.month=date.getMonth()+1;
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
		}
	}
</script>

<style>
	.content{
		width: 100%;
	}
	
	.header-wrap{
		width: 100%;
		height: 50px;
	}
	.left-text{
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
		font-size: 16px;
	}
	.month-text{
		width: 30px;
		height: 100%;
		text-align: center;
		font-weight: bold;
	}
	.text-content{
		height: 100%;
		flex: 1;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin: 3rpx;
	}
	.week-txt{
		width: 100%;
		height: 60%;
		text-align: center;
		font-size: 16px;
		font-weight: bold;
	}
	.date-txt{
		width: 100%;
		height: 40%;
		text-align: center;
		font-size: 14px;
	}
	/* 课表 */
	.table-wrap{
		width: 100%;
		height: 90%;
		display: flex;
		flex-direction: row;
		align-items: center;
	}
	.time{
		width: 30px;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		background-color: #ffd7ff;
	}
	.time-text{
		width: 100%;
		flex: 1;
		font-size: 14px;
		text-align: center;
		display: flex;
		align-items: center;
		justify-content: center;
		margin: 3rpx;
	}
	
	.class-item{
		flex: 1;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-left: 3rpx;
	}
	.class-text{
		width: 100%;
		flex: 2;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin: 3rpx;
		border-radius: 10rpx;
	}
	.class-text-noon{
		width: 100%;
		flex: 1;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin: 3rpx;
		border-radius: 10rpx;
	}
	.class-text-night{
		width: 100%;
		flex: 3;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin: 3rpx;
		border-radius: 10rpx;
	}
	.class-name{
		font-size: 16px;
		text-align: center;
		color: #ffffff;
	}
</style>
