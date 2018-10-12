# ReadMe

## 2018.10.11. Meeting

+ 11.7. 中期答辩 前期文献调研，方案制定 迅速建立 讨论（和企业导师多进行交流）

## Tasks

+ 简介：[基于信令数据的人口时空分布预测模型构建  任务说明（公司方）](https://github.com/BigDataSystemTHU2018/Project-Unicom/blob/master/IntroBrief.md) 

+ 任务描述：通过历史的人口时空分布数据，来预测未来的人口时空分布~具体说的话，通过北京六环以内，1km网格尺度的分天分小时人口分布数据（历史数据的时间跨度可以拉长到3个月）预测未来一周 相应网格下**每天每小时** 的人口分布（给出的数据是其实是信号的分布数据 不过一般认为一个设备就代表一个人了）（数据量，六环内差不多2000多个网格，但从初始数据量而言不大，但是对于其深入挖掘和处理却是难点）
  + 可能难点：
    + 首先，手机的信号数据（网格是1km）直接对应人口分布是否可以接受 
    + 另外，三个月的时间长度是不是足够预测一周，或者预测一周需要多久的数据（可能需要提出新的数据要求或者调整目标）
    + 对于人口分布的预测，不会只和历史数据有关系，是否需要得到对应的季节和天气的变化等额外会对分布有影响的数据（有哪些数据可能会影响？怎么得到？）
    + 注意：数据 会包含空间信息 单纯考虑时间会有问题 比如西单的人口量跟周围 清华的人口量跟周围之间  会有一定的关系（对于数据的理解角度和维度是否有别的理解）
+ 前期调研
  + 参考文献：
    + [城市计算_微软](https://www.microsoft.com/en-us/research/project/urban-computing/)
    + 代表文献：
      + [Deep Spatio-Temporal Residual Networks for Citywide Crowd Flows Prediction (Code,Slides,Pdf)](https://www.microsoft.com/en-us/research/publication/deep-spatio-temporal-residual-networks-for-citywide-crowd-flows-prediction/)
    + [一个城市计算的相关资料的汇总](https://www.zhihu.com/question/25359731)

## Schedule

+ 分工

  + 前期（**11.7.** 前完成）
    + 前期文献调研和分析
    + 方案设计和初步实践

+ 组员基本技能情况调研

  + 肖飞宇：熟练掌握**Latex** 可总体负责文档编写，会一定的C++，Python以及机器学习和人工智能的算法可以帮助一些代码构建和分析（负责总体协调）
  + 牛苒
  + 沈磊
  + 荆科
  + 赵嘉欣：会c++，python以及机器学习等算法
  + 李司棋
  + 张玉生
  + 韦承志

