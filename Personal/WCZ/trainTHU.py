'''
本模块为网络的训练模块
'''
import tensorflow as tf
import os
import numpy as np
from DeepST_by_CZ import ResnetTHU
from DeepST_by_CZ import getdataTHU


# 设置图片大小
IMAGE_WIDTH = 53
IMAGE_HIGHT = 54
# 最近的3张图
NUM_CHANNELS1 = 3
# 一天前的4张图
NUM_CHANNELS2 = 4
# 一周前的2张图
NUM_CHANNELS3 = 2

# 一次预测一个小时，即放入1张图片作为期望输出
BATCH_SIZE1 = 1
# 取最近的3个小时
BATCH_SIZE2 = 3
# 取一天前的4个小时
BATCH_SIZE3 = 4
# 取一周前的2个小时
BATCH_SIZE4 = 2

# 模型保存在当前路径
MODEL_SAVE_PATH = os.getcwd()
# 模型名称
MODEL_NAME = 'DST_by_CZ'

def backward(data, size_data):
    '''
    定义误差反向传播方法，采用adadelta优化方法(训练时可以改用adam)
    :param data: 输入数据
    :param size_data: 数据数据的总小时数
    :return:
    '''
    # 定义占位符，等待最近的3张图喂入
    x11 = tf.placeholder(tf.float32)
    # 输入reshape成网络要求的输入1代表一次喂入一组，3代表有3个通道
    x1_image = tf.reshape(x11, [
        1,
        IMAGE_HIGHT,
        IMAGE_WIDTH,
        3
    ])

    # 定义占位符，等待一天前4张图喂入
    x22 = tf.placeholder(tf.float32)
    x2_image = tf.reshape(x22, [
        1,
        IMAGE_HIGHT,
        IMAGE_WIDTH,
        4
    ])

    # 定义占位符，等待一周前的2张图喂入
    x33 = tf.placeholder(tf.float32)
    x3_image = tf.reshape(x33, [
        1,
        IMAGE_HIGHT,
        IMAGE_WIDTH,
        2
    ])

    # 定义占位符，等待期望输出y，一张图
    y_ = tf.placeholder(tf.float32)
    # y_image = tf.reshape(y_, [1, 54, 53, 1])
    # 最近3张图通过前向传播网络，得到结果y1
    y1 = ResnetTHU.forward(x1_image, NUM_CHANNELS1)
    # 一天前的4张图通过前向传播网络，得到结果y2
    y2 = ResnetTHU.forward(x2_image, NUM_CHANNELS2)
    # 一周前的2张图通过前向传播网络，得到结果y3
    y3 = ResnetTHU.forward(x3_image, NUM_CHANNELS3)
    # 三个结果相加
    y = y1 + y2 + y3
    # 把结果reshape成期望输出y_的样子
    Y = tf.reshape(y, [IMAGE_WIDTH * IMAGE_HIGHT])

    # 定义误差，均方误差
    mse = tf.reduce_mean(tf.square(y_ - y))

    # 定义优化器，即误差方向传播的算法，初始学习率为0.001，学习衰减指数为0.999
    train_step = tf.train.AdadeltaOptimizer(0.001, rho=0.999).minimize(mse)

    # 定义模型保存实例,设置最多保存30个模型
    saver = tf.train.Saver(max_to_keep=30)

    # 建立一个会话，在会话中作运算
    with tf.Session() as sess:
        # 初始化操作
        init_op = tf.global_variables_initializer()
        sess.run(init_op)

        # 如果有保存模型，则载入
        ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)

        # 预设轮数101
        epoch = 101
        STEPS = 0
        for ii in range(epoch):
            # 训练数据去掉头尾共两周
            for item in range(169, size_data - 168):
                # 取出1张作为期望输出
                start1 = item
                end1 = start1 + BATCH_SIZE1
                # 取出最近3张图
                start2 = item - 3
                end2 = start2 + BATCH_SIZE2
                # 取出一天前的4张图
                start3 = item - 27
                end3 = start3 + BATCH_SIZE3
                # 取出一周前的2张图
                start4 = item - 169
                end4 = start4 + BATCH_SIZE4

                x1 = data[start2:end2]
                size_x1 = len(x1[0])
                x2 = data[start3:end3]
                size_x2 = len(x2[0])
                x3 = data[start4:end4]
                size_x3 = len(x3[0])
                x1x = []
                x2x = []
                x3x = []
                # 把[[RRR],[BBB],[GGG]]格式改为[[RBG],[RBG],[RBG]]
                for i in range(size_x1):
                    for j in range(3):
                        x1x.append((x1[j][i]))
                for i in range(size_x2):
                    for j in range(4):
                        x2x.append((x2[j][i]))
                for i in range(size_x3):
                    for j in range(2):
                        x3x.append((x3[j][i]))


                x1x = np.array(x1x, dtype=np.float32)
                x2x = np.array(x2x, dtype=np.float32)
                x3x = np.array(x3x, dtype=np.float32)

                # 误差反向传播
                sess.run(train_step, feed_dict={x11: x1x, x22: x2x, x33: x3x, y_: data[start1:end1]})
                # 如果跟踪每一步的输出，则把标注去掉
                # YY = sess.run(Y, feed_dict={x11:x1x, x22:x2x, x33:x3x})
                # print(YY)
                # sess.run(train_step, feed_dict={x1: data[start2:end2], x2: data[start3:end3], x3: data[start4:end4],y_: data[start1:end1]})
                STEPS += 1
                # 每500步输出一次，跟踪结果
                if STEPS % 500 == 0:
                    loss = sess.run(mse, feed_dict={x11: x1x, x22: x2x, x33: x3x, y_: data[start1:end1]})
                    print('STEPS:{}, loss={}'.format(STEPS, loss))

            # 每10个epoch保存一次模型
            if ii % 10 == 0:
                print('epoch:{}'.format(ii))
                saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=STEPS)
def main():
    data, size = getdataTHU.get_files_data()
    backward(data, size)
if __name__ == '__main__':
    main()