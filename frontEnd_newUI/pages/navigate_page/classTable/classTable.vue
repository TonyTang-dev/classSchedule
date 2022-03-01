<template>
	<view class="content" :style="{height: windowHeight+'px'}">
		<view class="header-wrap" :style="{marginTop: barHeight+'px'}">
			<view class="left-text">
				<text class="month-text">{{month}}<br>月</text>
				<view :class="weeky==(i-1)?'text-content-today':'text-content'" v-for="i in 7" :key="i">
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
			<view :class="weeky==(index)?'class-item-today':'class-item'" v-for="(item,index) in classList" :key="index">
				<!-- 早上 -->
				<view 
					:class="[item.flex[j-1]==2?'class-text':'class-text-flex4']"
					v-for="j in item.flex[0]" :key="j"
					 :style="{backgroundColor: colorList()[item.id[j-1]]}" >
					 <view class="classTip-wrap">
						<text class="class-name">{{item.name[j-1]}}</text>
						<text class="classroom-text">{{item.classroom[j-1]}}</text>
					</view>
				</view>
				<!-- 中午 -->
				<view class="class-text-noon">
					<text class="class-name"></text>
				</view>
				<!-- 下午 -->
				<view
					:class="[item.flex[1]==2?'class-text':'class-text-flex4']"
					v-for="j in item.flex[1]" :key="j+3"
					 :style="{backgroundColor: colorList()[item.id[j-1+item.flex[0]]]}" >
					 <view class="classTip-wrap">
						 <!-- 索引列表去得到下午的课程 -->
						<text class="class-name">{{item.name[j-1+item.flex[0]]}}</text>
						<text class="classroom-text">{{item.classroom[j-1+item.flex[0]]}}</text>
					</view>
				</view>
				<!-- 晚上 -->
				<view
					class="class-text-night"
					 :style="{backgroundColor: colorList()[item.id[item.id.length-1]]}" >
					 <view class="classTip-wrap">
						 <!-- 索引列表去得到下午的课程 -->
						<text class="class-name">{{item.name[item.name.length-1]}}</text>
						<text class="classroom-text">{{item.classroom[item.name.length-1]}}</text>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				test: true,
				test2: false,
				month: 1,
				weeky: 1,
				week: ['周一','周二','周三','周四','周五','周六','周日'],
				date: [12,13,14,15,16,17,18],
				windowHeight: 800,
				barHeight: 30,
				
				classList: [
					{
						name: ['',"编译原理","数据库系统",'','企业法律风险管理'],
						classroom: ['',"D1443","D1215",'','D1135'],
						flex: [2,2,2],
						time: ["3-4","6-7"],	//暂时未使用
						id: [0,1,2,0,3]
					},
					{
						name: ['',"传感器网络与原理","Linux操作系统",'',''],
						classroom: ['',"D1443","D1447",'',''],
						flex: [1,1,3],
						time: ["1-2","11-13"],	//暂时未使用
						id: [0,4,5,0,0]
					},
					{
						name: ["","编译原理",'RFID原理及应用','',''],
						classroom: ["","D1443",'D1445','',''],
						flex: [2,2,2],
						time: ["3-4","6-7"],	//暂时未使用
						id: [0,1,6,0,0]
					},
					{
						name: ["","数据库系统",'','',''],
						classroom: ["","DZ312",'','',''],
						flex: [2,2,2],
						time: ["1-2","11-13"],	//暂时未使用
						id: [0,2,0,0,0]
					},
					{
						name: ['','','',"","传感器网络与原理"],
						classroom: ['','','',"","硬件实验室DS3305"],
						flex: [2,2,2],
						time: ["3-4","6-7"],	//暂时未使用
						id: [0,0,0,0,4]
					},
					{
						name: ["","",'编译原理',''],
						classroom: ["","",'硬件实验室DS3305',''],
						flex: [2,1,2],
						time: ["1-2","11-13"],	//暂时未使用
						id: [0,0,1,0]
					},
					{
						name: ["RFID原理及应用",'','',""],
						classroom: ["DS3305",'','',""],
						flex: [1,2,2],
						time: ["3-4","6-7"],	//暂时未使用
						id: [6,0,0,0]
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
			this.weeky=date.getDay();
		},
		
		methods: {
			//返回颜色
			colorList() {
				return [
					"#ffffff", //0
					"#ffaa00", //1
					"#33CC99",
					"#ff5500", //3
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
		margin-top: 5rpx;
		margin-left: 5rpx;
		margin-right: 5rpx;
	}
	.text-content-today{
		height: 100%;
		flex: 1;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin-top: 5rpx;
		margin-left: 5rpx;
		margin-right: 5rpx;
		background-color: #a5ffc9;
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
		background-color: #ffe5ff;
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
		overflow: hidden;	//直接在父元素价格overflow就解决了flex
	}
	.class-item-today{
		flex: 1;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-left: 3rpx;
		overflow: hidden;	//直接在父元素价格overflow就解决了flex
		background-color: #a5ffc9;
	}
	.class-text{
		width: 100%;
		flex: 2;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin-top: 5rpx;
		margin-left: 5rpx;
		margin-right: 5rpx;
		border-radius: 10rpx;
	}
	.class-text-flex4{
		width: 100%;
		flex: 4;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin-top: 5rpx;
		margin-left: 5rpx;
		margin-right: 5rpx;
		margin-bottom: 5rpx;
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
	.classTip-wrap{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.class-name{
		font-size: 14px;
		text-align: center;
		color: #ffffff;
	}
	.classroom-text{
		font-size: 12px;
		text-align: center;
		color: #ffffff;
	}
</style>
