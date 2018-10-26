# Project-Unicom
Project for Big data system foundation 2018

# Documents

+ Information.md: 关于项目的详细的资料和描述，需要大家经常关注更新

  + 每个成员首先在 **\Personal** 文件夹下的自己的md文档中记录自己的文献调研和问题进展(例如： feiyuxiao.md)，每次由组长汇总到根目录下的 Information.md 文档下供大家一起阅读
+ IntroBrief.md 主要记录公司方的项目需求
+ **\Refs** 目录下存放重要的文档和文献 **需要所有组员认真阅读** 

# Tools

+ 文档和代码的版本控制工具： **Git** 

  + [Git官网](https://git-scm.com/)
  + [廖雪峰的Git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000) （注意：主要学习 pull, commit的使用即可，代码开发可能需要 branch和merge的知识）
+ 文档写作 **Markdown**

  + 软件推荐： [Typora:windows,Mac都可以使用的免费Markdown语法编辑器](https://www.typora.io/)
  + 语法：
    + [Markdown简明语法](https://www.jianshu.com/p/191d1e21f7ed)
    + 详细的语法在**Typora** 软件中的 **Help->Markdown Reference** 有详细解答
+ Github 的使用

# Coding Tools

DeepST uses the following dependencies:

- [Keras](https://keras.io/#installation) and its dependencies are required to use DeepST. Please read [Keras Configuration](https://github.com/BigDataSystemTHU2018/DeepST/blob/master/keras_configuration.md) for the configuration setting.
- [Theano](http://deeplearning.net/software/theano/install.html#install) or [TensorFlow](https://github.com/tensorflow/tensorflow#download-and-setup), but **Theano** is recommended.
- numpy and scipy
- HDF5 and [h5py](http://www.h5py.org/)
- [pandas](http://pandas.pydata.org/)
- CUDA 7.5 or latest version. And **cuDNN** is highly recommended.

# Data of Beijing

[北京三个月六环内人口统计(password:THU201815)](https://cloud.tsinghua.edu.cn/d/b7c01ca65f624c7ab5db/)，涉及三个月的人口统计结果。里面有包含，六环内的1km网格数据，包括wkt格式的网格四至，以及shp图，再有就是基于联通人口统计得到的每日每时每网格的人口数，以及人口流入流出数。