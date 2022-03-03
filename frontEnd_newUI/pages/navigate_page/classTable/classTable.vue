<template>
	<view class="content" :style="{height: windowHeight+'px'}">
		<view class="header-wrap" :style="{marginTop: barHeight+'px'}">
			<view class="left-text">
				<text class="month-text">{{month}}<br>月</text>
				<view :class="weeky==(i)?'text-content-today':'text-content'" v-for="i in 7" :key="i">
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
				<text class="time-text" v-for="i in [6,7,8,9,10,11,12,13]" :key="i">{{i}}</text>
				<!-- <text class="time-text" >~</text> -->
			</view>
			<view :class="weeky==(index+1)?'class-item-today':'class-item'" v-for="(item,index) in classList" :key="index">
				<!-- 早上 -->
				<view 
					:class="[item.flex[0]==2?'class-text':'class-text-flex4']"
					v-for="j in item.flex[0]" :key="j"
					 :style="{backgroundColor: colorList()[item.id[j-1]],opacity: item.id[j-1]==0?0:1}"
					 @click="item.id[j-1]==0?null:clickClass(item,j-1)">
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
					 :style="{backgroundColor: colorList()[item.id[j-1+item.flex[0]]],opacity: item.id[j-1+item.flex[0]]==0?0:1}"
					 @click="item.id[j+item.flex[0]-1]==0?null:clickClass(item,j+item.flex[0]-1)">
					 <!-- 其中j+item.flex[0]-1是为了计算课程在数组中的索引 -->
					 <view class="classTip-wrap">
						 <!-- 索引列表去得到下午的课程 -->
						<text class="class-name">{{item.name[j-1+item.flex[0]]}}</text>
						<text class="classroom-text">{{item.classroom[j-1+item.flex[0]]}}</text>
					</view>
				</view>
				<!-- 晚上 -->
				<view
					class="class-text-night"
					 :style="{opacity: item.id[item.id.length-1]==0?0:1}" >
					 <view class="classTip-wrap" :style="{backgroundColor: colorList()[item.id[item.id.length-1]],
						height: item.flex[2]==2?50+'%':item.flex[2]==3?75+'%':100+'%'}"
						@click="item.id[item.id.length-1]==0?null:clickClass(item,item.id.length-1)">
						 <!-- 索引列表去得到下午的课程 -->
						<text class="class-name">{{item.name[item.name.length-1]}}</text>
						<text class="classroom-text">{{item.classroom[item.name.length-1]}}</text>
					</view>
				</view>
			</view>
		</view>
		
		<!-- 底部刷新按钮 -->
		<u-grid class="bottom-refresh-wrap"
			:border="false"
			col="5">
			<u-grid-item>
				<u-icon class="week-index-text" name="reload"
					color="#535353" size="20" @click="changePage(0)"></u-icon>
			</u-grid-item>
			<u-grid-item>
				<u-icon class="week-index-text" name="arrow-left"
					color="#535353" size="20" @click="changePage(1)"></u-icon>
			</u-grid-item>
			<u-grid-item>
				<text class="week-index-text" @click="changePage(4)">第 {{nowWeek}} 周</text>
			</u-grid-item>
			<u-grid-item>
				<u-icon class="week-index-text" name="arrow-right"
					color="#535353" size="20" @click="changePage(2)"></u-icon>
			</u-grid-item>
			<u-grid-item>
				<u-icon class="week-index-text" :name="perspectiveIcon"
					color="#535353" size="20" @click="changePage(3)"></u-icon>
			</u-grid-item>
		</u-grid>
		
		<!-- 课程详情 -->
		<u-modal :show="showMyModal"  title="课程详情" 
						:closeOnClickOverlay="true" 
						:showConfirmButton="false" @close="closeModal">
			<view class="slot-content">
				<u-cell-group>
					<u-cell
						v-for="(item,index) in modalItem" :key="index"
						:title="item"
						:icon="modalIcon[index]"
						:iconStyle="{color: colorList()[index+1]}"
						size="large"
					></u-cell>
				</u-cell-group>
			</view>
		</u-modal>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 第几周
				nowWeek: 1,
				perspectiveIcon: "grid",
				// 课表视图-一周/一学期
				tablePerspective: 0,
				// 课程详情
				showMyModal: false,
				modalItem: ['','','',''],//依次是课程名、教室、教师、上课时间--为了适配渲染
				modalIcon: ['calendar','home','server-man','clock'],
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
						teacher: ['',"陈咸章","吴开贵",'','乔兴旺'],
						flex: [2,2,3],
						time: ["3-4","6-7"],	//暂时未使用
						id: [0,1,2,0,3]
					},
					{
						name: ['',"传感器网络与原理","Linux操作系统",'',''],
						classroom: ['',"D1443","D1447",'',''],
						teacher: ['',"李艳涛","李双庆",'',''],
						flex: [2,2,0],
						time: ["1-2","11-13"],	//暂时未使用
						id: [0,4,5,0,0]
					},
					{
						name: ["","编译原理",'RFID原理及应用','',''],
						classroom: ["","D1443",'D1445','',''],
						teacher: ['',"陈咸章","刘卫宁",'',''],
						flex: [2,2,0],
						time: ["3-4","6-7"],	//暂时未使用
						id: [0,1,6,0,0]
					},
					{
						name: ["","数据库系统",'','',''],
						classroom: ["","DZ312",'','',''],
						teacher: ['',"吴开贵",'','',''],
						flex: [2,2,0],
						time: ["1-2","11-13"],	//暂时未使用
						id: [0,2,0,0,0]
					},
					{
						name: ['','','',"","传感器网络与原理"],
						classroom: ['','','',"","硬件实验室DS3305"],
						teacher: ['',"","",'','李艳涛'],
						flex: [2,2,4],
						time: ["3-4","6-7"],	//暂时未使用
						id: [0,0,0,0,4]
					},
					{
						name: ["","",'编译原理',''],
						classroom: ["","",'硬件实验室DS3305',''],
						teacher: ['',"","陈咸章",''],
						flex: [2,1,0],
						time: ["1-2","11-13"],	//暂时未使用
						id: [0,0,1,0]
					},
					{
						name: ["RFID原理及应用",'','',""],
						classroom: ["DS3305",'','',""],
						teacher: ['刘卫宁',"",'',''],
						flex: [1,2,0],
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
			
			// 课程详情
			clickClass(item, index){
				this.modalItem[0]="课程: "+item.name[index];
				this.modalItem[1]="教室: "+item.classroom[index];
				this.modalItem[2]="教师: "+item.teacher[index];
				this.modalItem[3]="时间: "+this.getTime(item,index);
				this.showMyModal=true;
			},
			getTime(item,index){
				switch(index){
					case 0:{
						if(item.flex[0]==1){
							return "8:30-12:10"
						}
						else{
							return '8:30-10:10'
						}
					}
					case 1:{
						if(item.flex[0]==1){
							if(item.flex[1]==1){
								return "14:25-18:05"
							}
							else{
								return '14:25-16:05'
							}
						}
						else{
							return '10:30-12:10'
						}
					}
					case 2:{
						if(item.flex[0]==1){
							if(item.flex[1]==1){
								if(item.flex[2]==2){
									return '19:00-20:40'
								}
								else if(item.flex[2]==3){
									return '19:00-21:35'
								}
								else{
									return '19:00-22:30'
								}
							}
							else{
								return '16:05:18:05'
							}
						}
						else{
							return '14:25-16:05'
						}
					}
					case 3:{
						if(item.flex[0]==1){
							if(item.flex[2]==2){
								return '19:00-20:40'
							}
							else if(item.flex[2]==3){
								return '19:00-21:35'
							}
							else{
								return '19:00-22:30'
							}
						}
						else{
							return '16:25-18:05'
						}
					}
					case 4:{
						if(item.flex[2]==2){
							return '19:00-20:40'
						}
						else if(item.flex[2]==3){
							return '19:00-21:35'
						}
						else{
							return '19:00-22:30'
						}
					}
				}
			},
			closeModal(){
				this.showMyModal=this.showMyModal==true?false:true;
			},
			
			// 切换课表周数
			changePage(index){
				switch(index){
					case 0:
						this.$u.toast("刷新课表");
						break;
					case 1:
						this.nowWeek==1?
							this.$u.toast("已经是第一周"):this.nowWeek=this.nowWeek-1;
						break;
					case 2:
						this.nowWeek==23?
							this.$u.toast("已经是最后一周"):this.nowWeek=this.nowWeek+1;
						break;
					case 3:
						this.tablePerspective=this.tablePerspective==0?1:0;
						this.perspectiveIcon=this.perspectiveIcon=="grid"?"calendar":"grid";
						this.$u.toast("切换课表视图");
						break;
					case 4:
						this.$u.toast("第"+this.nowWeek+"周");
						break;
				}
			}
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
		/* margin-top: 5rpx;
		margin-left: 5rpx;
		margin-right: 5rpx; */
		margin-left: 3rpx;
	}
	.text-content-today{
		height: 100%;
		flex: 1;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		/* margin-top: 5rpx;
		margin-left: 5rpx;
		margin-right: 5rpx; */
		margin-left: 3rpx;
		background-color: rgba(165,255,201,0.5);
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
		height: 100%;
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
		background-color: rgba(255,237,255,0.5);
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
		background-color: rgba(165,255,201,0.5);
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
		flex: 4;
		display: flex;
		flex-direction: column;
		align-items: center;
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
	
	/* 底部刷新部分按钮 */
	.bottom-refresh-wrap{
		width: 100%;
		height: 40px;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.week-index-text{
		font-size: 14px;
		flex: 1;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
	}
	
	/* modal */
	.slot-content{
		width: 100%;
	}
</style>
