import folium
import numpy as np
import pandas as pd

import webbrowser
from folium.plugins import HeatMap
import  folium.plugins as plugins

File1 = "output_fit"
Data = pd.read_csv(File1)
File2 = "GeoLabel.csv"
Geo = pd.read_csv(File2)
File3 = "grid2loc.csv"
grid = pd.read_csv(File3)

Geo = Geo.drop([0])  ## delete 12

Data = Data.values
Geo = Geo.values
grid = grid.values

data_move=[]
for i in range(24):
    Data0 = Data[i].reshape((54,53))

    lon = np.zeros(2264)
    lat = np.zeros(2264)
    people = np.zeros(2264)

    for i in range(2264):
        lon[i] = Geo[i][2]
        lat[i] = Geo[i][1]
        x = grid[i][2]
        y = grid[i][1]
        people[i] = Data0[x][y]
    population = [[lon[i],lat[i],people[i]] for i in range(2264)]
    data_move.append(population)

m = folium.Map(location=[lon.mean(),lat.mean()],tiles = 'OpenStreetMap',
                      control_scale=True,zoom_start=10)
#map_back.add_child(HeatMap(population,radius = 5, gradient={0.4:'blue',0.65:"lime",
#0.9:"red",1:'yellow'}))
hm = plugins.HeatMapWithTime(data_move,radius = 5,gradient={0.2:'green',0.4:'blue',0.6:'lime',0.75:'orange',0.9:'red'})
hm.add_to(m)
file_path = r"move.html"
hm.save(file_path)
webbrowser.open(file_path)

