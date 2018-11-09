import pandas as pd
import numpy as np
import os

'''首先读入grid2loc.csv确定每个基站数据放入一维向量的位置'''
coordi = pd.read_csv('grid2loc.csv',index_col=0)
#print(coordi.shape)
gridlocdict = {}    #字典：基站坐标--1d向量位置
for i in range(len(coordi)):
    grid = coordi.index[i]
    # 二维展成一维后的坐标， x_cor是列数，y_cor是行数
    loc1d = coordi.at[grid, 'x_cor'] + coordi.at[grid, 'y_cor'] * 53
    gridlocdict[grid] = loc1d
zerocoordi = [i for i in range(53 * 54) if i not in gridlocdict.values()]  # 将没有基站的1d坐标计入列表
zerocoordi_pd = pd.Series(zerocoordi,name='zerocoordinates')
zerocoordi_pd.to_csv('zerocoordi.csv',header=True,index=None)
#验证: print((len(zerocoordi)+len(gridlocdict)) == 54*53)
#注意：reshape时(54,53)
#！！！其实字典给的基站编号就是展成一维后的坐标，天啊！！！

'''对文件夹下的6个数据文件进行预处理'''
rootdir = '../raw_data'
data_files = os.listdir(rootdir)
for data_file in data_files:
    path = os.path.join(rootdir,data_file)

    data = pd.read_table(path)
    n = data.shape[0]  #原始数据行数
    #print(data)
    #a = data.iloc[0]
    #print(a['日期'])
    #print(data.iloc[0].dtype)
    #print(data['日期'][0].dtype)

    #找文件的：月份，最后第一天，最后一天
    month = (data.iloc[0,0]//100)%100
    firstday = data.iloc[0,0]%100
    lastday = data.iloc[-1,0]%100
    days_num = lastday-firstday+1

    '''转换成一个每行54*53的一维向量，按顺序放各基站驻留人数,
    每行对应一个timeslot，即一小时一行'''
    '''创建index'''
    index = []
    hournum=['%02d' %x for x in range(24)]
    for i in range(firstday,lastday+1):
        cur_day ='%02d' %month +'%02d' %i
        for j in range(24):
            index.append(cur_day+hournum[j])
    #print(index)

    '''创建dataframe'''
    finaldata = pd.DataFrame(np.full([days_num*24, 54*53],np.nan),index = index)
    #print(finaldata)

    '''录入value'''
    #把data中的，如20170901 0开头的数据,转换成以'090100'为index的一行数据
    for i in range(n):
        date = str(data.iloc[i,0])[4:]
        hour = '%02d' %data.iloc[i,1]
        grid = data.iloc[i,2]
        staynum = data.iloc[i,3]
        #print(grid,staynum,gridlocdict[grid])
        finaldata.at[date+hour,gridlocdict[grid]] = staynum
    #print(sum(np.isnan(finaldata.loc['090100'])))  >>>1733 (+ 1129 = 2862)
    #print(finaldata.loc['091123'])

    #把无基站列置0，数据缺失补上fill
    finaldata.at[:,zerocoordi]=0
    finaldata = finaldata.fillna(method='bfill')
    finaldata = finaldata.fillna(method='ffill')

    '''输出finaldata'''
    finaldata.to_csv( os.path.join('../preprocess_data',data_file+'_reshape.csv'))