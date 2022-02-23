<template>
	<view>
		<!-- 版权 -->
		<view class="copyright">
			<text>@Copyright Of YingFu</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
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
			
		}
	}
</script>

<style>
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
