# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:38:18 2018
json reader
@author: feiyuxiao
"""

import json

File = "GeoData.json"
with open(File,'r') as f:
    load_dict = json.load(f)
    print(load_dict)
f = open('GeoLabel.txt', 'w')

feature = load_dict['features']

for i in range(0,2265):
    attributes = feature[i]
    attribute = attributes["attributes"]
    Id = attribute['Id']
    lng = attribute['INSIDE_X']
    Lat = attribute['INSIDE_Y']
    list_ = [Id,lng,Lat]
    f.writelines(str(list_)+'\n')

f.close()
