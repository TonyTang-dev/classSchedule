<template>
	<view class="content">
		
		<view class="button-wrap">
			<!-- API按钮接口 -->
			<view class="APIset">
				<view class="APIRow">
					<view v-for="i in [0,1,2,3]" :key='i' class="temp-wrap">
						<view class="button-icon-temp" @click="clickAPI(i)">
							<view class="button-icon">
								<image class="button" :src="icon[i]"></image>
								<text class="APIname">{{APIname[i]}}</text>
							</view>
						</view>
					</view>
				</view>
			</view>
		</view>
		
		<model></model>
		
		<!-- 拍照按钮 -->
		<view class="take_wrap">
			<image class="take" @click="takePicture" src="../../static/takePhoto.png"></image>
		</view>
	</view>

</template>


<!-- 只能在APP和h5端运行 -->
<script>
	import model from "./header.vue"
	
	export default{
		data(){
			return{
				icon: ['../../static/schedule1.png', '../../static/newsAPI.png',
				 '../../static/map.png', '../../static/hairMall_select.png'],
				APIname:['发型设计','发色搭配','脸型修改','妆容设计'],
				
				
			}
		},
		
		components:{
			model,
		},
		
		methods:{
			//点击拍照按钮
			takePicture(){
				uni.navigateTo({
					url: '../navigate_page/hairMall/TakePicture/takePicture'
				});
				return;
			},
			
			// 点击按钮
			clickAPI(index){
				this.$u.toast("点击了按钮");
			}
		}
	}
</script>

<style>
	.content{
		display: flex;
		flex-direction: column;
	}
	
	//打开相册按钮
	.take_wrap{
		width: 100%;
		bottom: 30px;
		border-radius: 50%;
		position: fixed;
		display: flex;
		justify-content: center;
		z-index: 2;
	}
	.take{
		width: 72px;
		height: 72px;
		font-size: 14px;
	}
	
	/* 按钮层 */
	.button-wrap{
		width: 100%;
		z-index: 2;
		position: fixed;
		display: flex;
	}
	
	/* API按钮 */
	.APIset{
		margin-top: 20rpx;
		width: 100%;
		/* height: 200rpx; //因为我需要控件自适应，所以就不固定高度了，空间大小通过子控件的css来设定*/
		box-shadow: 0px 0px 0px 2px #f0fff2;
	}
	.APIRow{
		height: 130rpx;
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
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.button{
		width: 32px;
		height: 32px;
	}
	.APIname{
		font-size: 14px;
	}
	
	
</style>

