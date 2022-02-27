
<template>
	<view class="content">
		<view class="input-wrap">
			<input class="input" @input="inputContent" v-model="Content" placeholder="请输入昵称" maxlength="10"/>
			<text class="count">{{wordCount}}</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				wordCount: 10,
				Content: ''
			}
		},
		
		onNavigationBarButtonTap(e) {
			if(e.text=="保存"){
				this.$u.toast("点击了保存")
			}
		},
		
		methods: {
			//字数限制
			inputContent(e){
				this.wordCount -= 1;
				var count = e.detail.value.length;
				this.wordCount = 10-count;
			}
		}
	}
</script>

<style>
	.content{
		width: 100%;
		height: 100%;
	}
	
	.input-wrap{
		width: 100%;
		height: 3em;
		display: flex;
		flex-direction: row;
		align-items: flex-end;
		justify-content: space-between;
		border-style: none none solid none;
		border-width: 1px;
		border-color: #0000FF;
	}
	.input{
		font-size: 16px;
		padding-left: 5rpx;
	}
	.count{
		font-size: 16px;
		padding-right: 5rpx;
		color: #909399;
	}
</style>
