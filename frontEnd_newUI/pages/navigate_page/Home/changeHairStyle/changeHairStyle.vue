<template>
    <view class="content">
		<view class="effect-wrap">
			<image class="effect" src="../../../../static/effect_woman.png"></image>
			<view class="button-wrap" @click="changeImg">
				<button class="changeImg">
					<image class="changeImgIcon" src="../../../../static/add.png"></image>
					更换图片
				</button>
			</view>
		</view>
		
		<!-- 滑动窗口界面 -->
		<view class="slideWin">
			<swiperTabHead class="Tag" :tabBars="tabBars" :tabIndex="tabIndex" @tabtap="tabtap"></swiperTabHead>
			<view class="tab-bar">
				<swiper class="swiper-box"  :current="tabIndex" @change="tabChange">
					<swiper-item v-for="i in [0,1,2,3,4]" :key="i">
						<scroll-view scroll-y="true" class="list">
							<!-- <image src="../../../../static/takePhoto.png"></image> -->
							<view class="resource" v-for="i in 10" :key="i">
								<view class="resource-wrap">
									<image class="img" v-for="j in 5" :key="j" @click="selectHair(i,j)" src="../../../../static/head_man2.png"></image>
								</view>
							</view>
						</scroll-view> 
					</swiper-item>
				</swiper>
			</view>
		</view>
		<view class="gender-wrap">
			<icon type="clear" size="14" @click="clickButton(1)"></icon>
			<swiperTabGender class="Tag2" :tabBars="gender" :tabIndex="tabGender" @tabtap="clickGender"></swiperTabGender>
			<icon type="success" size="14" @click="clickButton(2)"></icon>
		</view>
    </view>
</template>

<script>
	//导入自定义组件--滑动窗口
	import swiperTabHead from "../../../swipeTab/swipeTab_changeHair.vue";
	import swiperTabGender from "../../../swipeTab/swipeTab_changeHair_gender.vue";
	
	export default {
		data() {
			return {
				//滑动界面的参数
				tabIndex: 0,// 选中的
				tabBars: [
					{ name:"夏天超A",id:"0" },
					{ name:"圆脸必选",id:"1" },
					{ name:"显发量",id:"2" },
					{ name:"易打理",id:"3" },
					{ name:"短发",id:"4" },
				],
				
				gender:[{ name:"男",id:"0" },
					{ name:"女",id:"1" },],
				tabGender:0
			}
		},
		onLoad(){
			
		},
		onShow(){		//通过onshow每次刷新评论的显示
			
		},
		
		//注册组件
		components:{
			 swiperTabHead,
			 swiperTabGender,
		},
		
		methods:{
			changeImg(){
				this.$u.toast("点击了更换图片")
			},
			
			//接受子组件传过来的值点击切换导航
			tabtap(index){
				this.tabIndex = index;
			},
			clickGender(index){
				this.tabGender = index;
			},
			//滑动切换导航
			tabChange(e){
			   this.tabIndex = e.detail.current;
			},
			tabChange2(e){
			   this.tabGender = e.detail.current;
			},
			
			//选择发型
			selectHair(i,j){
				this.$u.toast("点击了坐标（"+i+","+j+")");
			},
			
			//点击两个图标按钮
			clickButton(index){
				index==1?this.$u.toast("点击了取消按钮"):this.$u.toast("点击了确认按钮")
			}
		}
	}
</script>

<style>
	.content{
		flex-direction: column;
		align-items: center;
		display: flex;
		width: 100%;
		height: 100%;
	}
	//效果图
	.effect-wrap{
		flex-direction: column;
		align-items: center;
		display: flex;
		margin-left: 3px;
		margin-right: 3px;
		border-style: groove;
		width: 100%;
		height: 305px;
	}
	.effect{
		z-index: -1;
		position: fixed;
		width: 100%;
		height: 300px;
	}
	
	//更换图片按钮
	.button-wrap{
		display: flex;
		align-self: flex-end;
		margin: 5px;
	}
	.changeImg{
		border-radius: 20px;
		font-size: 14px;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.changeImgIcon{
		width: 14px;
		height: 14px;
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
	
	//可选内容
	.resource-wrap{
		display: flex;
		flex-direction: row;
	}
	.img{
		width: 54px;
		height: 90px;
		border-radius: 5px;
		margin: 5px;
	}
	
	//性别
	.gender-wrap{
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
		width: 100%;
		margin: 5px;
	}
</style>
