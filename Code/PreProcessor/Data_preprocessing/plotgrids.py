import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import MultipleLocator as mpl
import matplotlib.cm
import numpy as np

#利用热力图展示网格分布
data = pd.read_csv('loc2grid.csv',header=0,index_col=0)
data[data>0]=1
nrow=data.shape[0]
ncol=data.shape[1]
#print(data)

xlabel = np.arange(ncol+1)
ylabel = np.arange(nrow+1)

fig,ax = plt.subplots()
cmap = cm.get_cmap('rainbow',2)
im = ax.imshow(data,cmap=cmap)

xmajor = mpl(5)
ymajor = mpl(5)

ax.set_xticks(np.arange(ncol+1)-0.5,minor=True)
ax.set_yticks(np.arange(nrow+1)-0.5,minor=True)
ax.xaxis.set_major_locator(xmajor)
ax.yaxis.set_major_locator(ymajor)
#ax.set_xticklabels(xlabel)
#ax.set_yticklabels(ylabel)
ax.set_xlabel('Station Localization Map')
ax.grid(which='minor',color='w',linewidth=1)

ax.tick_params(top=True,bottom=False,labeltop=True,labelbottom=False)

plt.show()
