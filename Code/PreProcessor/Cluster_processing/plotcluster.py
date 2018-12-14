import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colorbar
from matplotlib.ticker import MultipleLocator as mpl
import matplotlib.cm
import numpy as np

#利用热力图展示网格分布
with open('groupK3.txt','r') as f:
    data = eval(f.read())
data = [list(map(lambda x:eval(x),item)) for item in data] #change str to int
clusters = len(data)

datamap = np.zeros((2862),dtype=np.uint8)
for i in range(clusters):
    datamap[data[i]]=i+1

bugs = [1913,1860,1914,1754,1915,1806,1866,1966,2017,1863]
datamap[bugs]=2
datamap = datamap.reshape((54,53))


xlabel = np.arange(53+1)
ylabel = np.arange(54+1)

fig,ax = plt.subplots()
cmap = cm.get_cmap('rainbow',clusters+1)
im = ax.imshow(datamap,cmap=cmap)

cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Different clusters', rotation=-90, va="bottom")
cbar.set_ticks([0,1,2,3,4,5])

xmajor = mpl(5)
ymajor = mpl(5)

ax.set_xticks(np.arange(53+1)-0.5,minor=True)
ax.set_yticks(np.arange(54+1)-0.5,minor=True)
ax.xaxis.set_major_locator(xmajor)
ax.yaxis.set_major_locator(ymajor)
#ax.set_xticklabels(xlabel)
#ax.set_yticklabels(ylabel)
ax.set_xlabel('Station Cluster(3 classes) Map')
ax.grid(which='minor',color='w',linewidth=1)

ax.tick_params(top=True,bottom=False,labeltop=True,labelbottom=False)

plt.show()
