# 使用python获取地图城市间距离

## 缘起：
一直没有完成第0周的任务，现在突然手上有一个任务，是老婆的工作，她希望能够获得地图上两个城市间的距离。
由于数据较多，希望批量处理，我觉得这个任务用python做是非常有趣的，因此自告奋勇，也作为我第0周的任务。

## 简化1：计算地图两点之间的距离

1. 计算距离公式：x1(经度,纬度)-x2(经度,纬度)
2. 自动获取地名相对应的经纬度值  
3. 建立一个dict={城市名:(经度,纬度)...} 这样一个字典
4. 输出


## 基本信息：
## [天地图](http://www.tianditu.cn/)
这是老婆在使用的数据，先看了一下代码
```
<script type="text/javascript" src="http://api.tianditu.com/js/maps.js"></script>
<script>
09
    var map;
10
    var zoom = 12;
11
    function onLoad()
12
    {
13
        //初始化地图对象
14
        map=new TMap("mapDiv");
15
        //设置显示地图的中心点和级别
16
        map.centerAndZoom(new TLngLat(116.40969,39.89945),zoom);
17
    }

    function getMapCenter()
20
    {
21
        alert("当前地图中心点：" + map.getCenter().getLng() + "," + map.getCenter().getLat());
22
    }
```
很明显，基于 maps.js 用TMap  getLng() 和 getLat()分别是经纬度获取方法

从另一端代码中可以看到，获取经纬度可以用 TLngLat(经度，纬度) 正是我们所希望的。
```
var marker = new TMarker(new TLngLat(116.411794,39.9068))
```
继续搜索天地图，获取 distance的计算信息，无法获得。转战google map
用google搜索，发现 google map 有专门的[python API](https://developers.google.com/api-client-library/python/apis/mapsengine/v1)
又觉得计算distance 应该是一件必须的事情，要不驾车路线如何给我们估计距离呢？
又见到一篇文章：
[自己计算distance ](http://blog.csdn.net/mad1989/article/details/9933089)
这样，计算没有问题了。
还是对[baidu API](http://developer.baidu.com/map/index.php?title=webapi/guide/webservice-geocoding)
有python API 心存期盼，毕竟国内用百度方便，只是搜索无果。
回到google python API

