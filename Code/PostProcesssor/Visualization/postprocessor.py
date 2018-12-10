# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:57:19 2018

@author: xiaofeiyu
"""
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

File = "output_fit"
Data = pd.read_csv(File)

Data = Data.values

Data0 = Data[0].reshape((54,53))    
fig = plt.figure()

x = list(range(0,53))
y = list(range(0,54))
X,Y = np.meshgrid(x,y)
df = pd.DataFrame(Data0)
heatmap_plot = sns.heatmap(df, center=5000,robust=True,linewidths=.005,cmap='rainbow')
plt.title('Distribution of Population in Beijing')
plt.savefig('test.png',dpi=200)


'''
for i in range(0,167):
    Data0 = Data[i].reshape((53,54))
    
    fig = plt.figure()
    ax = Axes3D(fig)
    x = list(range(0,54))
    y = list(range(0,53))
    X,Y = np.meshgrid(x,y)
    

    ax.plot_surface(X, Y, Data0, rstride=10, cstride=10, cmap=plt.get_cmap('rainbow'))
  
    name = str(i)+'.png' 
    
    
    
    plt.savefig(name,dpi=200)
    plt.close()
'''
