import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima_model import ARIMA

def test_stationarity(timeseries,title,figure_nb):
    # 决定起伏统计
    rolmean = timeseries.rolling(window=24).mean()    # 对size个数据进行移动平均
    #rol_weighted_mean = pd.ewma(timeseries, span=12)    # 对size个数据进行加权移动平均
    rolstd = timeseries.rolling(window=24).std()      # 偏离原始值多少
    # 画出起伏统计
    plt.figure(figure_nb)
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    #weighted_mean = plt.plot(rol_weighted_mean, color='green', label='weighted Mean')
    std = plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.xticks(rotation=20)
    plt.savefig('./Rolling mean std'+title+'.jpg')

    # 进行df测试
    print ('Result of Dickry-Fuller test')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical value(%s)' % key] = value
    dfoutput.to_csv('result.csv',mode='a+')
    print (dfoutput)

# 分解decomposing
def decomp(ts):
    decomposition = seasonal_decompose(ts)
    trend = decomposition.trend  # 趋势
    seasonal = decomposition.seasonal  # 季节性
    residual = decomposition.resid  # 剩余的

    plt.figure(4)
    plt.subplot(411)
    plt.title('Decomposition')
    plt.plot(ts,label='Original')
    plt.legend(loc=1); plt.xticks(rotation=20)
    plt.subplot(412)
    plt.plot(trend,label='Trend')
    plt.legend(loc=1); plt.xticks(rotation=20)
    plt.subplot(413)
    plt.plot(seasonal,label='Seasonarity')
    plt.legend(loc=1); plt.xticks(rotation=20)
    plt.subplot(414)
    plt.plot(residual,label='Residual')
    plt.legend(loc=1); plt.xticks(rotation=20)

    plt.tight_layout()
    plt.savefig('decompo.jpg')

def acf_pacf(ts):
    # 确定参数
    lag_acf = acf(ts, nlags=20)
    lag_pacf = pacf(ts, nlags=20)
    # q的获取:ACF图中曲线第一次穿过上置信区间.这里q取2
    plt.figure(5)
    plt.subplot(121)
    plt.plot(lag_acf)
    plt.axhline(y=0, linestyle='--', color='gray')
    plt.axhline(y=-1.96 / np.sqrt(len(ts)), linestyle='--', color='gray')  # lowwer置信区间
    plt.axhline(y=1.96 / np.sqrt(len(ts)), linestyle='--', color='gray')  # upper置信区间
    plt.title('Autocorrelation Function')
    # p的获取:PACF图中曲线第一次穿过上置信区间.这里p取2
    plt.subplot(122)
    plt.plot(lag_pacf)
    plt.axhline(y=0, linestyle='--', color='gray')
    plt.axhline(y=-1.96 / np.sqrt(len(ts)), linestyle='--', color='gray')
    plt.axhline(y=1.96 / np.sqrt(len(ts)), linestyle='--', color='gray')
    plt.title('Partial Autocorrelation Function')
    plt.tight_layout()
    plt.savefig('ACF & PACF')

def arma_models(ts):
    model = ARIMA(ts_log, order=(2, 1, 0))
    result_AR = model.fit(disp=-1)
    #plt.figure(6)
    #plt.plot(ts)
    #plt.plot(result_AR.fittedvalues, color='red')
    #plt.title('AR model RSS:%.4f' % sum(result_AR.fittedvalues - ts) ** 2)

    model = ARIMA(ts_log, order=(0, 1, 5))
    result_MA = model.fit(disp=-1)
    #plt.figure(7)
    #plt.plot(ts)
    #plt.plot(result_MA.fittedvalues, color='red')
    #plt.title('MA model RSS:%.4f' % sum(result_MA.fittedvalues - ts) ** 2)

    #model = ARIMA(ts_log, order=(2, 1, 3))
    #result_ARIMA = model.fit()
    #plt.figure(8)
    #plt.plot(ts)
    #plt.plot(result_ARIMA.fittedvalues, color='red')
    #plt.title('ARIMA RSS:%.4f' % sum(result_ARIMA.fittedvalues - ts) ** 2)
    return result_AR, result_MA

def predict_insample(model_result,figure_nb):
    predictions_diff = pd.Series(model_result.fittedvalues, copy=True)
    # print(predictions_ARIMA_diff.head())#发现数据是没有第一行的,因为有1的延迟

    predictions_diff_cumsum = predictions_diff.cumsum()
    # print (predictions_ARIMA_diff_cumsum.head())

    predictions_log = pd.Series(ts_log.ix[0], index=ts_log.index)
    predictions_log = predictions_log.add(predictions_diff_cumsum, fill_value=0)
    # print predictions_ARIMA_log.head()

    predictions = np.exp(predictions_log)
    plt.figure(figure_nb)
    plt.plot(ts,label='origin')
    plt.plot(predictions,label='prediction')
    plt.xticks(rotation=20)
    plt.legend(loc=0)
    plt.title('predictions_ARIMA RMSE: %.4f' % np.sqrt(sum((predictions - ts) ** 2) / len(ts)))

def predict_future(result_model,start_val):
    predict_diff = result_model.predict('2017-9-16 00:00:00','2017-9-23 23:00:00')
    predict_diff_cumsum =predict_diff.cumsum()
    predict_log=pd.Series(start_val,index=predict_diff.index)
    predict_log=predict_log.add(predict_diff_cumsum,fill_value=0)
    predict = np.exp(predict_log)

    plt.figure(11)
    plt.plot(ts,color='blue')
    plt.plot(data0.loc[pd.Timestamp(2017,9,16):pd.Timestamp(2017,9,23,23)],color='green')
    plt.plot(predict,color='red')
    plt.title('predictions(future)')

def predict_future_2():
    ar1=0.406
    ar2=0.081
    ar3=-0.065
    before = ts_log_diff.iloc[-3:]
    pred_diff = before.values.tolist()
    for i in range(24):
        pred_diff.append(pred_diff[-1]*ar1+pred_diff[-2]*ar2+pred_diff[-3]*ar3)

if __name__ == "__main__":
    data0 = pd.read_csv('timeseries.csv', index_col=0, header=None, names=['people'])
    data0.index = pd.to_datetime(data0.index, format='%Y-%m-%d %H:%M:%S')   #转换为datetime格式
    data = data0.loc[pd.Timestamp(2017,10,7):pd.Timestamp(2017,10,21,23,0,0)]

    ts = data['people']    #原始数据
    #test_stationarity(ts,' origin',1)
    '''取log'''
    ts_log = np.log(ts)
    #plt.figure(2)
    #plt.plot(ts_log)
    '''差分'''
    ts_log_diff = ts_log.diff(1)
    ts_log_diff.dropna(inplace=True)
    ts_diff = ts.diff(1)
    ts_diff.dropna(inplace=True)
    #test_stationarity(ts_log_diff,' log_diff',3)

    #decomp(ts_log)
    #acf_pacf(ts_log_diff)


    result_ar,result_ma= arma_models(ts_log)
    predict_insample(result_ar,9)
    predict_insample(result_ma,10)
    print('ar: ',result_ar.params)
    print('ma: ',result_ma.params)
    #predict_future(result_ar,ts_log.iloc[-1])

    plt.show()



