import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator as mpl
import datetime
from datetime import datetime as dtime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

data1 = pd.read_csv('../preprocess_data/month9a_reshape.csv',header=0,index_col=0)
data2 = pd.read_csv('../preprocess_data/month9b_reshape.csv',header=0,index_col=0)
data = pd.concat([data1,data2]) #按列拼接
#print(data.shape[0])

'''
# (15,30)为中心的25个格子
indexs = []; center=pd.Series((15,30))
for i in range(-2,3):
    for j in range(-2,3):
        point = pd.Series((i,j))+center
        indexs.append(53*point[0]+point[1])
#print(indexs)

ndays=7
data_part = data.iloc[:24*ndays,indexs]
result = data_part.apply(lambda x:x.sum(),axis=1) #按行求和
'''

#作图
ax = plt.subplot(111)

ndays=1
index = [53*15+30,53*15+31]
result1 = data.iloc[:24*ndays,index[0]]
result2 = data.iloc[:24*ndays,index[1]]
#生成时间序列
start = dtime.strptime('090100','%m%d%H')
end = dtime.strptime('09'+ '%02d' %ndays +'23','%m%d%H')
print(end)
dates = []
dates.append(start)
while start<end:
    start += datetime.timedelta(hours=+1)
    dates.append(start)
print(dates)

#指定X轴的以日期格式（带小时）显示
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d-%H'))
#X轴的间隔为天
ax.xaxis.set_major_locator(mdates.HourLocator(interval = 2))
#字符串旋转  没成功啊啊啊！
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_horizontalalignment('right')

plt.plot(dates, result1.values,c='b')
plt.plot(dates, result2.values,c='r')
plt.legend(labels=['grid(15,30)','grid(15,31)'])

#plt.gcf().autofmt_xdate()

plt.xlabel('Time')
plt.ylabel('Crowd/person')
plt.title('Graph of comparing crowd flow in 2 grids on Sep.1st 2017')
plt.show()




