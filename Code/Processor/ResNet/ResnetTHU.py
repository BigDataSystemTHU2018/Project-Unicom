'''
该模块为前向传播网路，定义网络结构
'''
import tensorflow as tf

CONV_SIZE = 5#卷积核大小

# 各层通道数
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

# 生成卷积核，权重w
def get_weight(shape, regularizer=None):
    '''生成卷积核，卷积核形状shape,权重w由正态分布产生'''
    w = tf.Variable(tf.truncated_normal(shape, stddev=0.01))
    if regularizer != None:
        tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(regularizer)(w))
    return w

# 生成偏置项
def get_bias(shape):
    '''初始化0偏置项b'''
    b = tf.Variable(tf.zeros(shape))
    return b

def conv2d(x,w):
    '''
    定义卷积操作
    x:输入图片
    w:卷积核
    strides:移动步长，左右上下移动步长为1
    padding:0填充操作，为了卷积操作后图片维度与原来相等
    '''
    return tf.nn.conv2d(x, w, strides=[1, 1, 1, 1], padding='SAME')


# 定义前向传播网络，按照文章的ResNet
def forward(x, channel, regularizer=None):

    # 第1个卷积层
    conv1_w = get_weight([CONV_SIZE, CONV_SIZE, channel, CONV1_KERNEL_NUM], regularizer)
    conv1_b = get_bias([CONV1_KERNEL_NUM])
    conv1 = conv2d(x, conv1_w)
    conv1_op = tf.nn.bias_add(conv1, conv1_b)

    # 第1个激活
    relu1 = tf.nn.relu(conv1_op)

    # 第2个卷积层
    conv2_w = get_weight([CONV_SIZE, CONV_SIZE, CONV1_KERNEL_NUM, CONV2_KERNEL_NUM], regularizer)
    conv2_b = get_bias([CONV2_KERNEL_NUM])
    conv2 = conv2d(relu1, conv2_w)
    conv2_op = tf.nn.bias_add(conv2, conv2_b)

    # 第2个激活
    relu2 = tf.nn.relu(conv2_op)

    # 第3个卷积层
    conv3_w = get_weight([CONV_SIZE, CONV_SIZE, CONV2_KERNEL_NUM, CONV3_KERNEL_NUM], regularizer)
    conv3_b = get_bias([CONV3_KERNEL_NUM])
    conv3 = conv2d(relu2, conv3_w)
    conv3_op = tf.nn.bias_add(conv3,conv3_b)

    # 第1个add层
    add1 = tf.add(conv3_op, conv1_op)

    # 第3个激活层
    relu3 = tf.nn.relu(add1)

    # 第4个卷积层
    conv4_w = get_weight([CONV_SIZE, CONV_SIZE, CONV3_KERNEL_NUM, CONV4_KERNEL_NUM], regularizer)
    conv4_b = get_bias([CONV4_KERNEL_NUM])
    conv4 = conv2d(relu3, conv4_w)
    conv4_op = tf.nn.bias_add(conv4, conv4_b)

    # 第4个激活层
    relu4 = tf.nn.relu(conv4_op)

    # 第5个卷积层
    conv5_w = get_weight([CONV_SIZE, CONV_SIZE, CONV4_KERNEL_NUM, CONV5_KERNEL_NUM], regularizer)
    conv5_b = get_bias([CONV5_KERNEL_NUM])
    conv5 = conv2d(relu4, conv5_w)
    conv5_op = tf.nn.bias_add(conv5, conv5_b)

    # 第2个add层
    add2 = tf.add(conv5_op, add1)

    # 第5个激活层
    relu5 = tf.nn.relu(add2)

    # 第6个卷积层
    conv6_w = get_weight([CONV_SIZE, CONV_SIZE, CONV5_KERNEL_NUM, CONV6_KERNEL_NUM], regularizer)
    conv6_b = get_bias([CONV6_KERNEL_NUM])
    conv6 = conv2d(relu5, conv6_w)
    conv6_op = tf.nn.bias_add(conv6, conv6_b)

    # 第6个激活层
    relu6 = tf.nn.relu(conv6_op)

    # 第7个卷积层
    conv7_w = get_weight([CONV_SIZE, CONV_SIZE, CONV6_KERNEL_NUM, CONV7_KERNEL_NUM], regularizer)
    conv7_b = get_bias([CONV7_KERNEL_NUM])
    conv7 = conv2d(relu6, conv7_w)
    conv7_op = tf.nn.bias_add(conv7, conv7_b)

    # 第3个add层
    add3 = tf.add(conv7_op, add2)

    # 第7个激活层
    relu7 = tf.nn.relu(add3)

    # 第8个卷积层
    conv8_w = get_weight([CONV_SIZE, CONV_SIZE, CONV7_KERNEL_NUM, CONV8_KERNEL_NUM], regularizer)
    conv8_b = get_bias([CONV8_KERNEL_NUM])
    conv8 = conv2d(relu7, conv8_w)
    conv8_op = tf.nn.bias_add(conv8, conv8_b)

    # 第8个激活层
    relu8 = tf.nn.relu(conv8_op)

    # 第9个卷积层
    conv9_w = get_weight([CONV_SIZE, CONV_SIZE, CONV8_KERNEL_NUM, CONV9_KERNEL_NUM], regularizer)
    conv9_b = get_bias([CONV9_KERNEL_NUM])
    conv9 = conv2d(relu8, conv9_w)
    conv9_op = tf.nn.bias_add(conv9, conv9_b)

    # 第4个add层
    add4 = tf.add(conv9_op, add3)

    # 第9个激活层
    relu9 = tf.nn.relu(add4)

    # 第10个卷积层
    conv10_w = get_weight([CONV_SIZE, CONV_SIZE, CONV9_KERNEL_NUM, CONV10_KERNEL_NUM], regularizer)
    conv10_b = get_bias([CONV10_KERNEL_NUM])
    conv10 = conv2d(relu9, conv10_w)
    conv10_op = tf.nn.bias_add(conv10, conv10_b)

    # 第10个激活层
    relu10 = tf.nn.relu(conv10_op)

    # 第11个卷积层
    conv11_w = get_weight([CONV_SIZE, CONV_SIZE, CONV10_KERNEL_NUM, CONV11_KERNEL_NUM], regularizer)
    conv11_b = get_bias([CONV11_KERNEL_NUM])
    conv11 = conv2d(relu10, conv11_w)
    conv11_op = tf.nn.bias_add(conv11, conv11_b)

    # 第5个add层
    add5 = tf.add(conv11_op, add4)

    # 第11个激活层
    relu11 = tf.nn.relu(add5)

    # 第12个卷积层
    conv12_w = get_weight([CONV_SIZE, CONV_SIZE, CONV11_KERNEL_NUM, CONV12_KERNEL_NUM], regularizer)
    conv12_b = get_bias([CONV12_KERNEL_NUM])
    conv12 = conv2d(relu11, conv12_w)
    conv12_op = tf.nn.bias_add(conv12, conv12_b)

    # 输出结果
    return conv12_op
