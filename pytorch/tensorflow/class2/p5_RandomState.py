import numpy as np

rdm = np.random.RandomState(seed=1)
a = rdm.rand()  # 返回一个随机标量
b = rdm.rand(2,3)   # 返回维度为2行3列随机数矩阵
print("a:",a)
print("b:",b)