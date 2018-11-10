import tensorflow as tf
import os
import csv
import numpy as np

MODEL_SAVE_PATH = os.getcwd()
MODEL_NAME = 'MODEL_3_10_10_3'
batch_size = 100 # 一次喂入神经网络多少数据

# 定义网络结构
x = tf.placeholder(tf.float32, name='week-ID-time')
y_ = tf.placeholder(tf.float32, name = 'NUMS-GONUMS-REANUMS')

w1 = tf.Variable(tf.random_normal([3,10], stddev=1), name = 'w1')
b1 = tf.Variable(tf.constant(0., shape=[10]), name = 'b1')
y1 = tf.nn.relu(tf.matmul(x, w1) + b1)

w2 = tf.Variable(tf.random_normal([10,10], stddev=1), name = 'w2')
b2 = tf.Variable(tf.constant(0., shape=[10]), name = 'b2')
y2 = tf.nn.relu(tf.matmul(y1, w2) + b2)

w3 = tf.Variable(tf.random_normal([10,3], stddev=1), name = 'w3')
b3 = tf.Variable(tf.constant(0., shape=[3]), name = 'b3')
y3 = tf.matmul(y2, w3) + b3


# 定义误差
mse = tf.reduce_mean(tf.square(y_ - y3))

train_step = tf.train.GradientDescentOptimizer(0.0001).minimize(mse)
# 实例化模型保存saver
saver = tf.train.Saver()


# 读取csv
csvFile = open('y2017nodate_normalzation.csv', 'r')

reader = csv.reader(csvFile)

result = {}

i = 0
for item in reader:
    if reader.line_num == 1:
        continue
    result[i] = item
    i += 1
data_size = i + 1

j = 0

xx = {}
yy = {}

for i in list(range(len(result))):
    xx[j] = result[i][1:4]
    yy[j] = result[i][4:]
    j += 1

csvFile.close()

del result

X = []
Y = []

for i in xx.values():
    X.append(i)

for j in yy.values():
    Y.append(j)

    
    

del xx
del yy

    

# 在Session中运算
with tf.Session() as sess:
    # Session初始化
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    # 打印初始化参数
    print('初始参数'.center(30,'*'))
    print('w1: \n', sess.run(w1))
    print('b1: \n', sess.run(b1))
    print('w2: \n', sess.run(w2))
    print('b2: \n', sess.run(b2))
    print('w3: \n', sess.run(w3))
    print('b3: \n', sess.run(b3))
    print('*'*30)

    STEPS = 500000
    for i in range(STEPS+1):
        start = (i*batch_size) % data_size
        end = min(start + batch_size, data_size)
        sess.run(train_step, feed_dict={x:X[start:end],y_:Y[start:end]})
        if i % 5000 == 0:
            total_loss = sess.run(mse,feed_dict={x:X,y_:Y})
            print('After {} traning step(s), loss on all data is {}'.format(i,total_loss))

        if i % 50000 == 0:
            saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=i)
    # 打印最终参数
    print('最终参数'.center(30,'*'))
    print('w1: \n', sess.run(w1))
    print('b1: \n', sess.run(b1))
    print('w2: \n', sess.run(w2))
    print('b2: \n', sess.run(b2))
    print('w3: \n', sess.run(w3))
    print('b3: \n', sess.run(b3))

