'''
此模块用来批量读取文件，将待测试的数据以csv或者txt格式放在次模块所在目录内。
'''
import os
import csv

global data
cumdata = []
global size
cumsize = 0

def read_csv_data(filename):
    global cumdata
    global cumsize
    try:
        csvFile = open(filename, 'r')
        reader = csv.reader(csvFile)
        for item in reader:
            cumdata.append(item)
            cumsize += 1
        csvFile.close()
    except:
        print('{}导入失败！'.format(filename))
    else:
        print('{}导入完毕！'.format(filename))

def get_data(filename_list):
    '''
    :return: data, size_data,数据和数据的条目数
    '''
    for file in filename_list:
        read_csv_data(file)
    return cumdata, cumsize

def get_files_data():
    '''
    读取目录下的csv、txt文件
    :return:下一步操作，获取数据
    '''
    file_list = os.listdir()
    txt_list = []
    for file in file_list:
        txt = os.path.splitext(file)[-1]
        if txt in ('.csv', '.txt'):
            txt_list.append(file)
    if txt_list == []:
        raise Exception('in get_files_data')
        return
    print('要依次读取的文件为：')
    for csv in txt_list:
        print(csv, end='\t')
    n = input('\n (y/n)')
    if n == 'y':
        return get_data(txt_list)

