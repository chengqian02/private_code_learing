import tensorflow as tf
# tf.one_hot(待转换数据,depth=几分类)
classes = 3
labels = tf.constant([1, 0, 2, 3])
output = tf.one_hot(labels, depth=4)
print(labels)
print(output)