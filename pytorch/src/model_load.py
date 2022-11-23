# author: hcx

import torch

# 加载方式1
model1 = torch.load("../save/vgg16_method1.pth")
print(model1)
# 加载方式2


model2 = torch.load("../save/vgg16_method2.pth")
print(model2)