# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:57:19 2018

@author: xiaofeiyu
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


File = "output_fit"
Data = pd.read_csv(File)

Data = Data.values

Data0 = Data[0].reshape((54,53))    

fig = plt.figure()
ax = fig.gca(projection='3d')

fig = plt.figure()
ax = Axes3D(fig)


x  = list(range(0,53))
y  = list(range(0,54))
X, Y = np.meshgrid(x, y)

for xdata in x:
  y = list(range(0,54))
  z = Data0[:,xdata]

  pos=ax.bar(y,z,xdata,align='center',zdir='y',color=["deepskyblue","lightgreen",'coral'],
              alpha=0.8)
 
ax.set_xlabel("X-Label")
ax.set_ylabel("Y-Label")
ax.set_zlabel("Z-Label")

title = "bar plot of population in Beijing"
plt.title(title)
plt.savefig("bar_plot"+".jpg",dpi=200)
#plt.show()

plt.close()
   

'''
images = []
filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('gif.gif', images,duration=0.25)
'''