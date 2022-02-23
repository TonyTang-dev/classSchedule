<template>
	<view>
		<view class="searchWord">
			<view class="tempWrap">
				<input class="searchInput" v-model="wordText" type="text" placeholder="请输入要查询的单词" />
				<icon class="searchButton" type="search" size="17" @click="clickSearch"></icon>
			</view>
		</view>
		<view class="swiperContent">
			<view class="page-section-spacing">
				<swiper class="swiper" :indicator-dots="indicatorDots" :autoplay="autoplay" :interval="interval" :duration="duration">
					<swiper-item>
						<image class="swiper-item" @click="selectPoster(1)" src="../../../static/englishBank1.png"></image>
					</swiper-item>
					<swiper-item>
						<image class="swiper-item" @click="selectPoster(2)" src="../../../static/englishBank2.png"></image>
					</swiper-item>
				</swiper>
			</view>
		</view>
		<!-- 注意事项等 -->
		<view class="appDetail">
			<view class="detailButton" v-for="i in [0,1,2]" :key="i" @click="clickDetail(i)">
				<image class="buttonIcon" :src="buttonIcon[i]"></image>
				<text class="buttonText">{{detailButton[i]}}</text>
			</view>
		</view>
		
		<!-- 版权 -->
		<view class="copyright">
			<text>@Copyright Of YingFu</text>
		</view>
	</view>
</template>

<script>
	//导入单词json
	import glossary from "../../../vocabulary/glossary.json";
	export default {
		data() {
			return {
				indicatorDots: true,
				autoplay: true,
				interval: 5000,
				duration: 500,
				
				//细节按钮
				buttonIcon:['../../../static/bank6.png','../../../static/bank4.png','../../../static/testTime.png'],
				detailButton:['六级单词','四级单词','考试时间'],
				
				//查单词
				wordText:'',
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
			//点击查单词
			clickSearch(){
				var _this=this;
				
				if(this.wordText==""){
					uni.showToast({
						title:'请输入单词再查询哦',
						icon:'none'
					});
					return;
				}
				
				for(var i=0;i<(glossary.vocabulary.length);i++){
					if(glossary.vocabulary[i].word==this.wordText){
						uni.showModal({
							title:_this.wordText,
							content:glossary.vocabulary[i].paraphrase,
							showCancel:false
						});
						_this.wordText="";
						return;
					}
				}
				uni.showToast({
					title:'当前词库没有此单词哦',
					icon:'none'
				});
				_this.wordText="";
				return;
			},
			//轮播图点击事件
			selectPoster(index){
				//第一张图片跳转到背单词解密那
				if(index==1){
					uni.navigateTo({
						url:'reciteWords/reciteWords',
					});
					return;
				}
				else{
					uni.showModal({
						title:"四六级考试时间",
						content:"日期:2021年12月18日\n四级:9:00-11:20\n六级:15:00-17:25",
						showCancel:false
					});
				}
			},
			
			//点击细节按钮
			clickDetail(index){
				if(index==0||index==1){
					uni.navigateTo({
						url:'reciteWords/reciteWords',
					});
					return;
				}
				else{
					uni.showModal({
						title:"四六级考试时间",
						content:"日期:2021年12月18日\n四级:9:00-11:20\n六级:15:00-17:25",
						showCancel:false
					});
				}
			},
		}
	}
</script>

<style>
	//查单词
	.searchWord{
		margin: 3px;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
	}
	.tempWrap{
		margin: 3px;
		height: 30px;
		display: flex;
		flex-direction: row;
		align-items: center;
		border-radius: 4px;
		box-shadow: 0px 0px 2px 2px #00ffff;
	}
	.searchInput{
		width: 100%;
		background-color: #ffffff;
		padding-left: 4px;
		font-size: 16px;
		font-weight: bold;
	}
	.searchButton{
		margin-right: 4px;
	}
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
	
	/* detail按钮 */
	.appDetail{
		font-size: 16px;
		margin-top: 20px;
	}
	.buttonIcon{
		width: 20px;
		height: 20px;
	}
	.buttonText{
		margin-left: 10px;
	}
	.detailButton{
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
</style>
