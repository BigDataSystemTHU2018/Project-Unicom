# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:57:19 2018

@author: xiaofeiyu
"""
import pandas as pd
import numpy as np
import os
import imageio
import seaborn as sns
from matplotlib import pyplot as plt

File = "output_fit"
Data = pd.read_csv(File)

Data = Data.values

x = list(range(0,53))
y = list(range(0,54))
X,Y = np.meshgrid(x,y)

for i in range(24):
    Data0 = Data[i].reshape((54,53))    
    fig = plt.figure()
    
    
    df = pd.DataFrame(Data0)
    heatmap_plot = sns.heatmap(df, center=5000,robust=True,linewidths=.005,cmap='rainbow')
    title = str(i)+'Distribution of Population in Beijing'
    plt.title(title)
    plt.savefig(chr(97+i)+".jpg",dpi=200)
    
    plt.close()

images = []
filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('heatmap_gif.gif', images,duration=0.2)