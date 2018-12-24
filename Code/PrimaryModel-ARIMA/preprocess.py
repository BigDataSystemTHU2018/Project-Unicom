import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

'''获得6个文件名'''
direc = r'E:\5研一上\大数据系统b\清华大学-人口预测\北京六环内人流情况统计9-10\北京六环内人流情况统计\统计结果\preprocess_data'
filecsv_list = [] #数据文件名
for _,_,files in os.walk(direc):
    for file in files:
        if os.path.splitext(file)[1]=='.csv':
            filecsv_list.append(file)

'''读取所需的几列数据'''
data = pd.DataFrame() #数据
center = 15*54+30   #网格号
col_indexs = [center-55,center-54,center-53,center,center-1,center+1,\
              center+53,center+54,center+55]
for csv in filecsv_list:
    cur_dir = os.path.join(direc,csv)
    data0 = pd.read_csv(cur_dir,header=0,index_col=0,engine='python')
    data = pd.concat([data,data0.iloc[:,col_indexs]])

data = data.sum(axis=1) #按行求和
data.index = pd.to_datetime(data.index,format='%m%d%H')
data.sort_index(inplace=True)   #按时间排序

delta = data.index-pd.Timestamp(1900,9,1)   #默认是1900年，转换为2017年
data.index = pd.Timestamp(2017,9,1)+delta
data.to_csv('timeseries.csv')

plt.plot(data)
plt.xticks(rotation=20)

'''
data_cut = data.loc[pd.Timestamp(2017,10,9),:]
plt.plot(data_cut)
plt.xticks(rotation=20)
'''
plt.show()