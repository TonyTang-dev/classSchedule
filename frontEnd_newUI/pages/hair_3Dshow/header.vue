<template>
	<!-- #ifdef APP-PLUS || H5 -->
	<view class="content" :style="{height: myHeight+'px'}">
		<view id="threeView"></view>
	</view>
	<!-- #endif -->
	<!-- #ifndef APP-PLUS || H5 -->
	<view>非 APP、H5 环境不支持</view>
	<!-- #endif -->

</template>


<!-- 只能在APP和h5端运行 -->
<script module="three" lang="renderjs">
	const THREE = require('static/three/build/three.min.js')
	
	// OrbitControls 是对 Threejs 的三维场景进行缩放、平移、旋转操作
	import {
		OrbitControls
	} from 'static/three/examples/jsm/controls/OrbitControls.js'

	// 导入 glb 格式模型，若要导入其他格式模型，可尝试在 loaders 目录下加载其他文件
	import {
		GLTFLoader
	} from 'static/three/examples/jsm/loaders/GLTFLoader.js'

	var renderer;
	var scene;
	var camera;
	var controls;

	export default {
		data(){
			return{
				myHeight: (window.innerHeight)/2
			}
		},
		
		mounted() {
			this.initThree();//加载场景
			this.leadModel();//导入模型
			this.createControls();//控制模型的缩放、平移、旋转操作

		},
		
		methods: {
			createControls() {
				controls = new OrbitControls(camera, renderer.domElement)
			},

			// 导入模型
			leadModel() {
				let loader = new GLTFLoader();
				
				// 通过条件编译完成不同端之间的协调
				// 导入本地或者服务器上的模型都可以
				//#ifdef H5
					loader.load('../../static/test2.gltf', function(gltf) {
					// loader.load('https://threejs.org/examples/models/gltf/RobotExpressive/RobotExpressive.glb', function(gltf) {
						scene.add(gltf.scene);
					});
				//#endif
				// APP-PLUS
				//#ifndef H5 
					loader.load('static/test2.gltf', function(gltf) {
					// loader.load('https://threejs.org/examples/models/gltf/RobotExpressive/RobotExpressive.glb', function(gltf) {
						scene.add(gltf.scene);
					});
				//#endif
			},

			initThree() {
				// 如果返回的不是未定义，说明threejs成功引入
				// console.log('打印场景API', THREE.Scene);

				/* 创建场景对象Scene */
				scene = new THREE.Scene();

				// 环境光
				var ambient = new THREE.AmbientLight(0xffffff);
				scene.add(ambient);

				/*
				    相机设置
				 */
				var width = window.innerWidth; // 窗口宽度
				var height = window.innerHeight; // 高度
				// var width = 300; // 窗口宽度
				// var height = 300; // 高度
				var k = width / height; // 窗口宽高比
				var s = 1000; // 三维场景显示范围控制系数，系数越大，显示的范围越大
				// 创建相机对象（正射投影）
				camera = new THREE.PerspectiveCamera(45, k, 1, 10000);
				camera.position.set(0, 0, 20); //设置相机的摆放位置
				camera.lookAt(new THREE.Vector3(0, 0, 0)); // 控制相机的焦点(镜头)位置，决定相机的朝向（取值为3维坐标对象-THREE.Vector3(x,y,z)）

				/*
				    创建渲染器对象
				 */
				renderer = new THREE.WebGLRenderer({
					antialias: true,
					// alpha: true //设置透明，为true时，背景颜色需要注释掉
				});

				renderer.setSize(width, height); // 设置渲染区域尺寸
				renderer.setClearColor(0XECF1F3, 1); // 设置背景颜色
				const element = document.getElementById('threeView')
				element.appendChild(renderer.domElement); // body元素中插入canvas对象
				// 执行渲染操作，指定场景，相机作为参数
				renderer.render(scene, camera);

				this.render();
			},

			// 动画
			render() {
				let that = this;
				requestAnimationFrame(function() {
					that.render();
				});
				renderer.render(scene, camera); //执行渲染操作
			},

		}
	}
</script>

<style>
	.content{
		width: 100%;
		position: fixed;
		/* height: 200px; */
		overflow: hidden;
		margin-top: 200rpx;
		border-style: groove;
		border-radius: 5%;
	}
</style>

