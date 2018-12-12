# ReadMe

## 数据文档说明

*GeoData.json* 为通过 [Arcgis](https://developers.arcgis.com/documentation/) 转化 shp 文件所得到的蕴含格点的经纬度坐标的文件

*GeoData.txt* 为读取分析 json 文件得到的格点编号和地理经纬度坐标对应的关系，*GeoData.csv* 为对应的csv文件

*output_fit* 为对于未来一周每天二十四小时的人口分布的预测结果

## 可视化手段

### 静态图形

分别绘制了 热力图(heatmap.png) 曲面图(surface_plot.jpg)和三维条形图(bar)

### 动态图形

基于静态图形的绘制，得到了动态图形(surface_plot.gif)和(heatmap_gif.gif)

其中获取 **gif** 图形的方法基于 [imageio](https://pypi.org/project/imageio/) 

```python
images = []
filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('surface_plot.gif', images,duration=0.25)
```

**注意** 其中对于图片的排序注意 python 中对于字符串的排序规则

### 和地图结合的可视化

应用 [Folium](https://github.com/python-visualization/folium) 包和 [Leaflet](https://leafletjs.com/) 地图进行可视化

分为静态 *heatmap_folium.py* (folium.html)和动态 *moveheatmap.py*(move.html)





