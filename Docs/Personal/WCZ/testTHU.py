'''
测试模块，请把输入文件改成9a, 9b, 10a, 10b,之类。
'''
import csv
import numpy as np
import os


def read_predicted(filename):
    '''
    读取待测试的数据
    :param filename: 文件名 请写成'fitXXXXX.txt'形式
    :return: 返回待测试数据的ndarray形式
    '''
    predicted = []
    size = 0
    f = open(filename, 'r')
    reader = csv.reader(f)
    for item in reader:
        item = item[0].split('\t')
        item = item[:-1]
        predicted.append(item)
        size += 1
    f.close()
    predicted_np = np.array(predicted, dtype=np.float32)
    return predicted_np, size

def read_real(predict_size, predict_days=7):
    '''
    读取真实数据，根据待预测的天数读取。加入数据有两年的，但是待预测的只有一周，也只会读入最后半个月的真实数据。
    :param predict_size: 待预测数据的大小，保证两者大小一致才能比较
    :param predict_days: 待预测的天数，保证读入的数据不会太多造成内存浪费
    :return: 返回真实数据的ndarray形式
    '''
    n = int(predict_days // 15 + 1)
    file_list = os.listdir()
    txt_list = []
    for file in file_list:
        txt = os.path.splitext(file)[-1]
        if (txt in ('.csv', '.txt')) and ('fit' not in file):
            txt_list.append(file)
    if txt_list == []:
        raise Exception('获取文件失败')
        return
    txt_list = sorted(txt_list, key=lambda x: int(x[:-5]))
    real = []
    real_size = 0
    for j in txt_list[-n:]:
        f = open(j, 'r')
        reader = csv.reader(f)
        for m in reader:
            real.append(m)
            real_size += 1
        f.close()
    real = real[real_size - predict_size:real_size]
    real_np = np.array(real, dtype=np.float32)
    return real_np

def get_interval(lst, nums=7*24):
    '''获得预测区间，默认为一周'''
    if len(lst) < nums:
        raise Exception('in get_interval')
    else:
        return lst[:nums]

def error_less_than(predicted_np, real_np, filler=50):
    if predicted_np.shape != real_np.shape:
        raise Exception('in error_less_than')
    else:
        di = np.abs(real_np - predicted_np)
        c = di < filler
        rate = c.sum() / real_np.size
        return rate, di.flatten()

def mse_less_than(predict_np, real_np, filler=50):
    if predict_np.shape != real_np.shape:
        raise Exception('in ems_less_than')
    else:
        len_out = len(predict_np)
        mse = np.zeros(len_out)
        len_in = len(predict_np[0])
        for i in range(len_out):
            a = (predict_np[i] - real_np[i])**2
            a = a.sum()
            each_ems = a / len_in
            mse[i] = each_ems
        c = mse < filler
        rate = c.sum() / len_out
        return rate, mse

def error_less_than_interval(filename, nums, max_days, filler=50):
    '''
    求绝对误差小于某个阈值的函数
    :param filename: 待预测文件
    :param nums: 小时数
    :param max_days: 最大天数
    :param filler: 阈值
    :return: 百分比，真实误差
    '''
    predict_data, predict_size = read_predicted(filename)
    real_data = read_real(predict_size, max_days)
    predict_interval = get_interval(predict_data, nums)
    real_interval = get_interval(real_data, nums)
    rate, error = error_less_than(predict_interval, real_interval, filler)
    return rate, error

def mse_less_than_interval(filename, nums, max_days, filler=50):
    '''
    求均方误差小于某个阈值的函数
    :param filename: 待预测的文件
    :param nums: 小时数
    :param max_days: 最大天数
    :param filler: 阈值
    :return: 百分比，均方误差
    '''
    predict_data, predict_size = read_predicted(filename)
    real_data = read_real(predict_size, max_days)
    predict_interval = get_interval(predict_data, nums)
    real_interval = get_interval(real_data, nums)
    rate, mse = mse_less_than(predict_interval, real_interval, filler)
    return rate, mse

def naive(hours=0):
    '''
    用插值方法来预测
    :param hours: 最后hours个小时不加入预测
    :return: 插值方法的预测值
    '''
    file_list = os.listdir()
    txt_list = []
    for file in file_list:
        txt = os.path.splitext(file)[-1]
        if (txt in ('.csv', '.txt')) and ('fit' not in file):
            txt_list.append(file)
    if txt_list == []:
        raise Exception('获取文件失败')
        return
    txt_list = sorted(txt_list, key=lambda x: int(x[:-5]))
    real = []
    real_size = 0
    for j in txt_list:
        f = open(j, 'r')
        reader = csv.reader(f)
        for m in reader:
            real.append(m)
            real_size += 1
        f.close()
    if hours == 0:
        real = np.array(real, dtype=np.float32)
    else:
        real = real[:-hours]
        real = np.array(real, dtype=np.float32)
        real_size -= hours
    naive_predict = np.zeros((hours, real.shape[-1]), dtype=np.float32)
    navie_list = []
    for i in range(hours):
        j = 0
        count = 0
        while -j <= (real_size - hours) :
            count += 1
            j -= 168
            a = naive_predict[i]
            b = real[j]
            c = a+b
            naive_predict[i] = c
        avg = naive_predict[i] / count
        avg = avg.tolist()
        navie_list.append(avg)
    return np.array(navie_list)

def main(predict_file,predict_hours, max_predict_days, filler=50):
    error_rate, error = error_less_than_interval(predict_file, predict_hours, max_predict_days, filler)
    mse_rate, mse = mse_less_than_interval(predict_file, predict_hours, max_predict_days, filler)
    print(error_rate)
    print(error)
    print(mse_rate)
    print(mse)
    print('*'*20)



if __name__ == '__main__':
    # main('fit1.txt', 168, 7)
    predict_data, predict_size = read_predicted('DST002_test_2ST_fit4.txt')
    print(predict_data.shape)

    real_data = read_real(predict_size, 7)
    print(real_data.shape)
    naive_predict = naive(168)
    print(naive_predict.shape)
    interval_predict = get_interval(predict_data, 168)
    print(interval_predict.shape)
    interval_real = get_interval(real_data, 168)
    print(interval_real.shape)
    interval_naive = get_interval(naive_predict, 168)
    print(interval_naive.shape)
    predict_error_rate_50, predict_error_50 = error_less_than(interval_predict, interval_real, 200)
    naive_error_rate_50, naive_error_50 = error_less_than(interval_naive, interval_real, 200)
    print(predict_error_rate_50)
    print(predict_error_50)
    print('*'*20)
    print(naive_error_rate_50)
    print(naive_error_50)
