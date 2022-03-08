<template>
	<view class="content">
		<view class="item" v-for="i in dynamicText.length" :key="i">
			<view class="myInfo-wrap">
				<view class="info-wrap">
					<image class="head-photo" :src="head_photo"></image>
					<view class="nick-wrap">
						<text class="nick">{{nick}}</text>
						<text class="time">{{time}}</text>
					</view>
				</view>
				<image class="menu" @click="menu" src="../../../../../../static/tri_dot.png"></image>
			</view>
			<view class="dynamicContent-wrap">
				<text class="text-content">{{dynamicText[i-1]}}</text>
				<image class="img" @click="imgDetail" :src="dynamicImg[i-1]" mode="aspectFill"></image>
			</view>
			<view class="op-wrap">
				<view class="like-wrap" @click="like">
					<image class="like icon" src="../../../../../../static/my_like.png"></image>
					<text class="like-text detail-text">赞</text>
				</view>
				<view class="comment-wrap like-wrap" @click="comment">
					<image class="comment icon" src="../../../../../../static/my_comment.png"></image>
					<text class="comment-text detail-text">评论</text>
				</view>
				<view class="share-wrap like-wrap" @click="share">
					<image class="share icon" src="../../../../../../static/my_share.png"></image>
					<text class="share-text detail-text">分享</text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				head_photo: "../../../../../../static/head_man1.png",
				nick: "兔子一号",
				time: "刚刚",
				
				dynamicText: ["测试文本1","测试文本2"],
				dynamicImg: ["../../../../../../static/head_man1.png","../../../../../../static/head_man2.png"]
			}
		},
		onNavigationBarButtonTap(button) {
			if(button.text=="拍照"){
				this.$u.toast("点击了拍照")
			}
		},
		
		methods: {
			menu(){
				this.$u.toast("点击了菜单")
			},
			like(){
				this.$u.toast("点击了点赞");
			},
			comment(){
				this.$u.toast("点击了评论")
			},
			share(){
				this.$u.toast("点击了分享")
			},
			
			//图片详情
			imgDetail(){
				this.$u.toast("点击了图片")
			},
		}
	}
</script>

<style>
	.content{
		width: 100%;
		height: 100%;
	}
	.item{
		display: flex;
		flex-direction: column;
		width: 100%;
		height: 800rpx;
		border-style: none none solid none;
		border-width: 1px;
		margin-bottom: 2px;
		border-color: #BBBBBB;
	}
	.myInfo-wrap{
		width: 100%;
		height: 50px;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
	}
	.info-wrap{
		display: flex;
		flex-direction: row;
	}
	.head-photo{
		width: 48px;
		height: 48px;
		margin-left: 3px;
		margin-right: 3px;
		border-radius: 5%;
	}
	.nick-wrap{
		height: 50px;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.nick{
		font-size: 14px;
		font-weight: bold;
	}
	.time{
		font-size: 14px;
		color: #BBBBBB;
	}
	.menu{
		width: 24px;
		height: 24px;
		margin-right: 5px;
	}
	
	.dynamicContent-wrap{
		flex: 1;
		display: flex;
		flex-direction: column;
	}
	.text-content{
		font-size: 16px;
		margin-left: 4px;
	}
	.img{
		width: 80%;
		/* height: 200px; */
		margin: 2px;
		border-style: groove;
		border-radius: 5%;
	}
	
	.op-wrap{
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		margin: 10px;
	}
	.like-wrap{
		display: flex;
		flex-direction: row;
		align-items: center;
	}
	.icon{
		width: 24px;
		height: 24px;
	}
	.detail-text{
		font-size: 16px;
	}
</style>
