# ReadMe

## 数据清洗



1. 确定基站编号与地理位置间的关系

之所以我们需要得到基站与网格分布的对应关系，是因为每个网格的人口数据不仅是时序的，还与空间分布有关。例如某网格人数的增加与周围网格人数减少相关。前期的数据预处理得到网格分布可能为后续预测提供方便。



2. 重新整理数据格式，并利用前后时刻添补了缺失数据

![](https://github.com/BigDataSystemTHU2018/Project-Unicom/blob/master/Personal/Jiaxin/Data_preprocessing/reshape.png)
3. 对整理后的数据进行简单可视化

![](https://github.com/BigDataSystemTHU2018/Project-Unicom/blob/master/Personal/Jiaxin/Data_preprocessing/month9_week1_25grids.png)
![](https://github.com/BigDataSystemTHU2018/Project-Unicom/blob/master/Personal/Jiaxin/Data_preprocessing/compare.png)

