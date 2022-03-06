<template>
	<view class="content">
		<view class="fixedView">
			<view class="searchWord">
				<view class="tempWrap">
					<input class="searchInput" v-model="wordText" type="text" placeholder="请输入要查询的单词" />
					<icon class="searchButton" type="search" size="17" @click="clickSearch"></icon>
				</view>
			</view>
		</view>
		<!-- 用一个白板把第一次刷新时的单词与搜索栏隔开 -->
		<view class="partition"></view>
		<view class="wordList" v-for="i in 100" :key="i">
			<view class="wordWrap" @click="clickWord(i,wordsText[i+glossaryIndex*100].word,wordsText[i+glossaryIndex*100].paraphrase)">
				<text class="number">{{i+100*glossaryIndex}}. </text>
				<text class="words"> {{wordsText[i+glossaryIndex*100].word}}  :  {{wordsText[i+glossaryIndex*100].paraphrase}}</text>
			</view>
		</view>
		
		<u-modal :show="showMyModal"  title="单词详情"
						:closeOnClickOverlay="true" 
						:showConfirmButton="false" @close="closeModal">
			<view class="slot-content" style="width: 100%;">
				<u-cell-group style="width: 100%;">
					<u-cell
						v-for="(item,index) in modalItem" :key="index"
						:title="item"
						:icon="modalIcon[index]"
						size="large"
						style="width: 100%;"
					></u-cell>
				</u-cell-group>
			</view>
		</u-modal>
	</view>
</template>

<script>
	import glossary from '../../../../../static/vocabulary/glossary.json';
	export default {
		data() {
			return {
				glossaryIndex:0,
				wordsText:glossary.vocabulary,
				
				showMyModal: false,
				modalItem: ['',''],//依次是课程名、教室、教师、上课时间--为了适配渲染
				modalIcon: ['calendar','home','server-man','clock'],
				
				//查单词
				wordText:'',
			}
		},
		onLoad(){
			
		},
		//导航栏按钮点击事件
		onNavigationBarButtonTap(button) {
			uni.showToast({
				title:button.text=="主页"?"点击主页":"点击退出",
				icon:"none"
			})
		},
		onPullDownRefresh() {
			//下拉刷新
			uni.showToast({
				title:"已经是第一页",
				icon:"none"
			});
			if(this.glossaryIndex>0){
				uni.showToast({
					title:"加载上一页单词",
					icon:"none"
				});
				this.glossaryIndex-=1;
			}
			uni.stopPullDownRefresh();
		},
		onReachBottom() {
			//上拉刷新
			uni.showToast({
				title:"已经是最后一页",
				icon:"none"
			});
			if(this.glossaryIndex<11){
				uni.showToast({
					title:"加载新单词",
					icon:"none"
				});
				this.glossaryIndex+=1;
			}
			else{
				this.glossaryIndex=0;
			}
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
			
			clickWord(index,eng,chinese){
				this.modalItem[0]="英: "+eng;
				this.modalItem[1]="汉: "+chinese;
				this.showMyModal=true;
			},
			closeModal(){
				this.showMyModal=this.showMyModal==true?false:true;
			},
		}
	}
</script>

<style>
	//查单词
	.fixedView{
		position: fixed;
		width: 100%;
		background-color: #ffffff;
	}
	.searchWord{
		height: 40px;
		margin-top: 5px;
		margin-bottom: 5px;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
	}
	.tempWrap{
		margin: 3px;
		height: 40px;
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
	
	/* 隔开 */
	.partition{
		width: 100%;
		height: 50px;
	}
	
	.content{
		width: 100%;
		height: 100%;
	}
	.wordList{
		height: 50px;
		width: 100%;
	}
	.wordWrap{
		width: 100%;
		height: 100%;
		margin-top: 3px;
		display: flex;
		flex-direction: row;
		align-items: center;
		box-shadow: 0px 0px 2px 2px #d2d9ff;
	}
	.number{
		padding-left: 4px;
		font-size: .7em;
		color: #007AFF;
	}
	.words{
		padding-left: 3px;
		font-size: 16px;
		overflow: hidden;
	}
</style>
