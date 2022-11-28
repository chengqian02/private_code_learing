import numpy as np

# np.mgrid[起始值:结束值:步长,起始值:结束值:步长,....]    // [起始值:结束值) 左开右闭区间
x,y = np.mgrid[1:3:1,2:4:0.5]
# x.ravel 将x变成一维数组
# np.c_[] 使返回的间隔数值点配对
grid = np.c_[x.ravel(), y.ravel()]
print("x:",x)
print("y:",y)
print(grid)