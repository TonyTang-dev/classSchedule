<template>
    <view class="tab-bar">
        <scroll-view class="swiper-tab" scroll-x="true">
			<view class="row">
				<view class="element" v-for="(tab,index) in tabBars" :key="tab.id">
					<view 
						class="tab-list" 
						:class="{'active' : tabIndex==index}"
						@tap="tabtap(index)">
						<text class="textTag">{{tab.name}} {{tab.num?tab.num:""}}</text>
						<view class="tab-line"></view>
					</view>
				</view>
			</view>
        </scroll-view>
    </view>
</template>

<script>
    export default {
		data(){
			return{
				
			}
		},
        props:{
            tabBars:Array,
            tabIndex:Number,
            
        },
        methods:{
            //点击切换导航
            tabtap(index){
                // this.tabIndex = index;
                this.$emit('tabtap',index)
            }
        }
    }
</script>　

<style scoped >
	.tab-bar{
		width: 100%;
		height: 100%;
	}
	.swiper-tab{
        border-bottom: 1upx solid #EEEEEE;
    }
    .tab-list{
        color: #aaaaff;
        /* font-weight: bold; */
		display: flex;
		flex-direction: column;
		align-items: center;
    }
	
	//标签栏标签
	.row{
		display: flex;
		flex-direction: row;
	}
	.element{
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 20%;
	}
	
	//标签文本
	.textTag{
		font-size: 14px;
		text-align: center;
	}
	
    .tab-bar .active{
        color: #000000;
    }
    .active .tab-line{
        border-bottom: 6upx solid #FEDE33;
        width: 100upx;
        /* margin: auto; */
        border-top: 6upx solid #FEDE33;
        border-radius: 20upx;
    }
</style>