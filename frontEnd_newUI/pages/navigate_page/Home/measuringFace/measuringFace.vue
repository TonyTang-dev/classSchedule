<template>
	<view class="content">
		<!-- 背景图片 -->
		<image class="bg"></image>
		<image class="logo" :src="myHeadPhoto" @click="clickFace"></image>
		<!-- 提示语 -->
		<text class="tips">智能分析 识别中···</text>
		
		<!-- 滑动窗口界面 -->
		<view class="slideWin">
			<swiperTabHead class="Tag" :tabBars="tabBars" :tabIndex="tabIndex" @tabtap="tabtap"></swiperTabHead>
			<view class="tab-bar">
				<swiper class="swiper-box"  :current="tabIndex" @change="tabChange">
					<swiper-item v-for="i in [0,1,2]" :key="i">
						<scroll-view scroll-y="true" class="list">
							<!-- <image src="../../../../static/takePhoto.png"></image> -->
							<!-- 分析结果等 -->
							<view class="appDetail">
								<!-- <scroll-view scroll-y="true" style="height: 100%;"> -->
									<view class="detailTextWrap" v-for="j in detailText[i].length" :key="j" @click="clickDetail(i,j-1)">
										<image class="textIcon" :src="textIcon[j-1]"></image>
										<text class="textText">{{detailText[i][j-1]}}</text>
									</view>
								<!-- </scroll-view> -->
							</view>
						</scroll-view> 
					</swiper-item>
				</swiper>
			</view>
		</view>
	</view>
</template>

<script>
	//导入自定义组件--滑动窗口
	import swiperTabHead from "../../../swipeTab/swipeTab.vue";
	
	export default {
		
		data() {
			return {
				myHeadPhoto: "../../../../static/head_man2.png",
				
				//滑动界面的参数
				tabIndex: 0,// 选中的
				tabBars: [
					{ name:"三庭测量",id:"0" },
					{ name:"脸部定位",id:"1" },
					{ name:"综合分析",id:"2" },
				],
				
				swiperheight:500,//高度
				
				//细节按钮
				textIcon:['../../../../static/myData.png','../../../../static/introduction.png','../../../../static/system.png',
					'../../../../static/introduction.png','../../../../static/system.png'],
				detailText:[["定位为头-眉峰-眉尾","定位眼长-眼高",
								"定位鼻高-鼻翼宽","定位嘴宽-嘴唇厚度",
								"脸型分析"],
							 ["上庭数据提取",'中庭数据提取',"下庭数据提取"],
							 ["推荐发型","识别年龄","评估颜值","综合评分"]
							],
			}
		},
			
		computed: {		
			
		},
		
		methods: {
			onShow(){
				
			},
			
			onLoad(){
				uni.getSystemInfo({
					success:(res)=>{
						let height = res.windowHeight-uni.upx2px(100)
						this.swiperheight = height;
					}
				})
			},
			
			//接受子组件传过来的值点击切换导航
			tabtap(index){
				this.tabIndex = index;
			},
			//滑动切换导航
			tabChange(e){
			   this.tabIndex = e.detail.current;
			},
			
			//点击细节按钮
			clickDetail(i,j){
				this.$u.toast("点击了"+this.detailText[i][j]);
			},
			
			//点击头像
			clickFace(){
				this.$u.toast("点击了头像")
			}
		},
		
		//注册组件
		components:{
			 swiperTabHead,
		},
	};
</script>

<style lang="scss" scoped>
	.content {					//父容器
		flex-direction: column;
		display: flex;
		align-items: center;
		align-content: center;
		width: 100%;
		height: 100%;
		
		//背景
		.bg{
			width: 100%;
			height: 100%;
			z-index: -1;
			position: fixed;		
			filter: blur(4rpx) brightness(70%);//模糊半径和变暗度
			background-image: url("../../../../static/bgSky.png");
		}
		
		.logo {					//头像
			height: 128px;
			width: 128px;
			margin-top: 200rpx;
			margin-left: auto;
			margin-right: auto;
			margin-bottom: 50rpx;
			border-radius: 50%;
			border-style: groove;
			-moz-box-shadow:0 0 3px 3px #06c;
			-webkit-box-shadow:0 0 3px 3px #06c;
			box-shadow:0 0 3px 3px #06c;
		}
		//提示文字
		.tips{
			margin-top: 100upx;
			margin-bottom: 100rpx;
			color: #ffffff;
			text-align: center;
			font-size: 14px;
			// border: medium double rgb(0, 85, 255);
			// background-color: #55557f;
			border-radius: 5px;
			border-style: groove;
		}
		
		//滑动页
		.slideWin{
			display: flex;
			flex-direction: column;
			width: 100%;
			height: 100%;
		}
		.list{
			width: 100%;
			// height: 80px;
			height: 100%;
		}
		.Tag{
			margin-top: 20upx;
			width: 100%;
			height: 100%;
		}
		
		/* detail文本 */
		.appDetail{
			font-size: 16px;
			margin-top: 10upx;
			display: flex;
			flex-direction: column;
			align-items: center;
		}
		.textIcon{
			width: 20px;
			height: 20px;
		}
		.textText{
			margin-left: 10px;
			font-size: 14px;
			color: #FFFFFF
		}
		.detailTextWrap{
			width: 80%;
			box-shadow: 0px 0px 0px 2px #fffced;
			margin-top: 10px;
			padding-left: 10px;
			display: flex;
			flex-direction: row;
			align-items: center;
			border-radius: 5px;
		}
		
		//滑动显示容器
		.tab-bar{
			height: 200px;
		}
		.swiper-box{
			/* height: 400px; */
			height: 100%;
		}
		
		.temp{
			height: 100%;
		}
		.list{
			width: 100%;
			// height: 80px;
			height: 100%;
		}
		.Tag{
			margin-top: 20upx;
			width: 100%;
			height: 100%;
		}
	}
</style>
