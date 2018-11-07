import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datas = pd.read_csv('bj_liuhuan_wkt.csv',skiprows = 1,names=['grid','points'])
n = len(datas)
#print(datas['grid'])

'''
# 简单看下网格的样子
fig = plt.figure(1)
print(datas['points'][0])
for i in range(len(datas)):
    data = datas['points'][i]
    # print(data)
    xs = []
    ys = []
    loc = data.find('(')
    xs.append(int(data[loc + 3:loc + 9]))
    ys.append(int(data[loc + 22:loc + 29]))
    data = data[loc + 42:]
    for i in range(3):
        xs.append(int(data[:6]))
        ys.append(int(data[19:26]))
        data = data[39:]

    plt.scatter(xs, ys,marker='.',s=2)
plt.show(fig)
'''

# 发现坐标更简单的规律,（433943.69714851433 4393540.4441694766），且只找一个网格的左上角
xs=[]; ys=[]
for i in range(len(datas)):
    data = datas['points'][i]   #Dataframe读取先列后行
    # print(data)
    loc = data.find('(')
    xs.append(int(data[loc + 4:loc + 6]))
    ys.append(int(data[loc + 23:loc + 26]))
xs=pd.Series(xs); ys=pd.Series(ys)
xs = xs-xs.min()
ys = ys-ys.min()

fig = plt.figure(1)
plt.scatter(xs,ys,marker='.',s=3)
plt.show(fig)

'''
# 找到编号对应的一个二维矩阵中的位置，即行列数值
xordi = xs.max()+1 #列数
yordi = ys.max()+1 #行数
grid2loc = pd.DataFrame(np.zeros((n,2),np.int8),index = datas['grid']) #类似字典形式 编号--坐标
loc2grid = pd.DataFrame(np.zeros((yordi,xordi),np.int16))  #二维矩阵形式 坐标--编号
for i in range(n):
    gridnumber = datas['grid'][i]
    point = (xs[i],ys[i])
    grid2loc.iat[i,0] = xs[i]
    grid2loc.iat[i,1] = ys[i]
    loc2grid.iat[ys[i],xs[i]] = gridnumber
# 保存成csv格式
grid2loc.to_csv('grid2loc.csv',index_label= 'stationID',header=['x_cor','y_cor'])
loc2grid.to_csv('loc2grid.csv')
#print(grid2loc)
#print(loc2grid)
'''






