import pandas as pd
import numpy as np
import os
'''只需要将rootdir修改为原始数据的目录即可'''

'''对文件夹下的6个数据文件进行预处理'''
zerocoordi = pd.read_csv('zerocoordi.csv',header=0).iloc[:,0].tolist()  #无数据的网格编号
rootdir = '../raw_data'
data_files = os.listdir(rootdir)

final = pd.DataFrame(columns=range(54*43))
for data_file in data_files:
    path = os.path.join(rootdir,data_file)
    data = pd.read_table(path)
    n = data.shape[0]  #原始数据行数

    '''格式转换成每行代表一小时，共54*53=2862数据,无数据网格补零'''
    startday = str(data.iloc[0,0])
    periods = 24*(data.iloc[-1,0]-data.iloc[1,0]+1)
    index = pd.date_range(start=startday,periods=periods,freq='H')    #生成index

    '''创建dataframe'''
    finaldata = pd.DataFrame(np.full([periods, 54*53],np.nan),index = index)

    '''录入value'''
    for i in range(n):
        date = str(data.iloc[i,0])
        hour = '%02d' %data.iloc[i,1]
        timeslot = pd.to_datetime(date + hour, format='%Y%m%d%H')
        grid = data.iloc[i,2]
        staynum = data.iloc[i,3]
        finaldata.at[timeslot, grid] = staynum

    #把无基站列置0，数据缺失用前后时刻补上
    finaldata.at[:,zerocoordi]=0
    finaldata = finaldata.fillna(method='bfill')
    finaldata = finaldata.fillna(method='ffill')
    final = pd.concat([final,finaldata])

'''输出finaldata'''
final.to_csv('../preprocess_data/data_reshape.csv')