'''
本模块为对ID进行聚类，聚类的条件为ID之间人口在时间变化上的某种相似性
'''

import csv
from collections import defaultdict
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

# 定义聚类函数
def clusterTHU(data_file, save_file, cluster=3):
    '''
    Kmeans聚类方法
    :param data_file: 输入数据文件路径及文件名
    :param save_file: 输出数据文件路径及文件名
    :param cluster: 要分成几类，默认3类
    :return:
    '''
    # 打开数据文件，文件格式为 ID,驻留人数，出发人数，到达人数
    csvFile = open(data_file, 'r')
    reader = csv.reader(csvFile)

    # 定义字典保存信息
    result = {}
    # 记录数据大小
    data_size = 0

    for item in reader:
        # 如果文件包含标题行的话，则把下面两行注释去掉，现在使用的文件没有包含标题行。
        # if reader.line_num == 1:
        #     continue
        result[data_size] = item
        data_size += 1

    # 建立一个默认值为list 的字典
    data = defaultdict(list)

    for i in range(data_size):
        data[result[i][0]].append(result[i][1])
        data[result[i][0]].append(result[i][2])
        data[result[i][0]].append(result[i][3])
    csvFile.close()

    # 释放内存
    del result


    ID = []
    NUMS = []
    for k,v in data.items():
        ID.append(k)
        NUMS.append(v)

    km = KMeans(n_clusters=cluster)
    label = km.fit_predict(NUMS)
    expenses = np.sum(km.cluster_centers_, axis=1)

    ID_Cluster = [[],[],[]]
    for i in range(len(ID)):
        ID_Cluster[label[i]].append(ID[i])

    for i in range(len(ID_Cluster)):
        print('Expenses:%.2f'% expenses[i])
        print(ID_Cluster[i])

    K3 = pd.DataFrame(data=ID_Cluster)
    K3.to_csv(save_file)
def main():

    data_file = 'y2017_group.csv'
    save_file = 'k3.txt'
    cluster_nums = 3
    clusterTHU(data_file, save_file, cluster_nums)
if __name__ == '__main__':
    main()