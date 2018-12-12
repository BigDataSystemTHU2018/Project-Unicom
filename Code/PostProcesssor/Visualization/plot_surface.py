# -*- coding: utf-8 -*-
"""
Create surface maps

@author: feiyuxiao
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import imageio



File = "output_fit"
Data = pd.read_csv(File)

Data = Data.values

for i in range(24):
    # 0 for example
    Data0 = Data[i].reshape((54,53))  
    
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # 创建 3D 图形对象
    fig = plt.figure()
    ax = Axes3D(fig)
    
    # 生成数据并绘图
    x  = list(range(0,53))
    y  = list(range(0,54))
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X,Y,Data0,rstride=1,cstride=1,cmap="Blues")
    
    title = str(i)+"Surface map of population distibution in Beijing"
    plt.savefig(chr(97+i)+".jpg",dpi=200)  
    plt.close()
   


images = []
filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('surface_plot.gif', images,duration=0.25)
