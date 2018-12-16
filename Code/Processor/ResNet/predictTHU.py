'''
本模块为预测模块，将模型训练完成后，运行本模块。得到预测结果。
结果为txt文件，一行代表一个小时。
相关参数的数字与 backwardTHU模块相同
'''
import tensorflow as tf
import os
import numpy as np
import getdataTHU
import ResnetTHU

# 要预测的天数
predic_days = 7
# 保存结果
save_name = 'check001.txt'


IMAGE_WIDTH = 53
IMAGE_HIGHT = 54
NUM_CHANNELS1 = 3
NUM_CHANNELS2 = 4
NUM_CHANNELS3 = 2

CONV_SIZE = 5

CONV1_KERNEL_NUM = 64
CONV2_KERNEL_NUM = 64
CONV3_KERNEL_NUM = 64
CONV4_KERNEL_NUM = 64
CONV5_KERNEL_NUM = 64
CONV6_KERNEL_NUM = 64
CONV7_KERNEL_NUM = 64
CONV8_KERNEL_NUM = 64
CONV9_KERNEL_NUM = 64
CONV10_KERNEL_NUM = 64
CONV11_KERNEL_NUM = 64
CONV12_KERNEL_NUM = 1

BATCH_SIZE1 = 1
BATCH_SIZE2 = 3
BATCH_SIZE3 = 4
BATCH_SIZE4 = 2

MODEL_SAVE_PATH = os.getcwd()
MODEL_NAME = 'DST_by_CZ'

def test(data, tra_arr, predict_start, predict_end):
    x11 = tf.placeholder(tf.float32)
    x1_image = tf.reshape(x11, [
        1,
        IMAGE_HIGHT,
        IMAGE_WIDTH,
        3
    ])

    x22 = tf.placeholder(tf.float32)
    x2_image = tf.reshape(x22, [
        1,
        IMAGE_HIGHT,
        IMAGE_WIDTH,
        4
    ])

    x33 = tf.placeholder(tf.float32)
    x3_image = tf.reshape(x33, [
        1,
        IMAGE_HIGHT,
        IMAGE_WIDTH,
        2
    ])
    y_ = tf.placeholder(tf.float32)
    y_image = tf.reshape(y_, [1, IMAGE_HIGHT, IMAGE_WIDTH, 1])
    y1 = ResnetTHU.forward(x1_image, NUM_CHANNELS1)
    y2 = ResnetTHU.forward(x2_image, NUM_CHANNELS2)
    y3 = ResnetTHU.forward(x3_image, NUM_CHANNELS3)
    y = y1 + y2 + y3
    y = y * tra_arr

    mse = tf.reduce_mean(tf.square(y_image - y))


    saver = tf.train.Saver()

    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        sess.run(init_op)
        
        # 如果已有模型保存下来，则启动已经保存好的模型，checkpoint为配置文件，修改checkpoint内的配置可以自由切换模型
        ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)

        STEPS = 0
        output_datas = []
        # 对最后一个周进行预测
        for item in range(predict_start, predict_end):
            start1 = item
            end1 = start1 + BATCH_SIZE1
            start2 = item - 3
            end2 = start2 + BATCH_SIZE2
            start3 = item - 27
            end3 = start3 + BATCH_SIZE3
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
            
            # 求出预测结果并打印输出
            YY = sess.run(y, feed_dict={x11: x1x, x22: x2x, x33: x3x})
            print(YY)
            # 将预测结果的二维结构拉直成一维，为了与输出作比较
            YYY = np.ravel(YY)
            print(YYY)
            YYY = YYY.tolist()
            # 将预测结果保存在output_datas变量，后面将该变量写入文件输出
            output_datas.append(YYY)

            STEPS += 1
            # 观察每一步输出的误差，真实情况下也许没有期望值，就必须把下面两行标注掉
            loss = sess.run(mse, feed_dict={x11: x1x, x22: x2x, x33: x3x, y_: data[start1:end1]})
            print('STEPS:{}, loss={}'.format(STEPS, loss))
            # 将本次的预测结果又作为下次预测的输入
            data[item] = YYY
        
        # 把所有预测结果写入文件输出
        with open(save_name, 'w') as f:
            len_out = predict_end - predict_start
            len_in = IMAGE_HIGHT * IMAGE_WIDTH
            for i in range(len_out):
                for j in range(len_in):
                    f.write(str(output_datas[i][j]))
                    f.write('\t')
                f.write('\n')
                
def predic_region(size_data, predic_days):
    '''
    返回一个预测区间，输入为图片总数，即总小时数，和待预测的天数
    :param size_data: 图片总数，即总小时数
    :param predic_days: 待预测的天数
    :return: 预测区间
    '''
    return size_data - predic_days*24, size_data

def output_updata(lst):
    '''
    返回一个输出修正矩阵对预测结果进行修正。因为真实图片存在补零点，修正将预测值还原
    :param lst: 输入数据
    :return: 修正矩阵
    '''
    tra_arr = []
    for nums in lst[0]:
        if nums !=0:
            nums = 1
        tra_arr.append(nums)
    tra_arr = tf.constant(tra_arr, dtype=tf.float32)
    return tra_arr

def main():
    # 读取数据
    data, size_data = getdataTHU.get_files_data()

    tra_arr = output_updata(data)
    # 把修正矩阵reshape成输出图片的形状
    tra_arr = tf.reshape(tra_arr, (1, IMAGE_HIGHT, IMAGE_WIDTH, 1))
    predict_start, predict_end = predic_region(size_data, predic_days)
    test(data, tra_arr, predict_start, predict_end)

if __name__ == '__main__':
    main()
