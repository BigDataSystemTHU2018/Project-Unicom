import pandas as pd
import matplotlib.pyplot as plt

index = pd.date_range(start = '2017-11-24',periods=168,freq='H')

predict0 = pd.read_csv("../data/DeepSTbyCZ_test_2st_fit1.txt",sep='\t',header=None)
predict0.drop(columns = [2862],inplace=True)
predict0.index=index

truth0 = pd.read_csv("../data/month11b_reshape.csv",header=0,usecols=range(1,2863))
truth0 = truth0.iloc[-168:,:]
truth0.index=index

grid = 1408
'''
1408---三里屯
1185---西站
1245---天安门
1751---中关村
中关村9格---[1714,1715,1716,1660,1661,1662,1804,1805,1806]  
'''
#predict = predict0[grid].apply(lambda x:x.sum(),axis=1)
#truth = truth0.iloc[:,grid].apply(lambda x:x.sum(),axis=1)
predict = predict0[grid]
truth = truth0.iloc[:,grid]
plt.figure(1)
plt.plot(predict,label='Predict')
plt.plot(truth,label='Truth')
plt.xlabel('date')
plt.ylabel('persons')
plt.legend(loc=0)
plt.title('Comparison between predict & truth value in Xizhan')
plt.show()
