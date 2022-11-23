# author: hcx
import tensorflow as tf
import numpy as np

# 生成均匀分布随机数
a = tf.random.uniform([2,3], maxval=1, minval=0)
print(a)
