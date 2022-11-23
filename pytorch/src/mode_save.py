# author: hcx

import torch
import torchvision

vgg16 = torchvision.models.vgg16(pretrained=False)

# 保存方式1 ， 保存模型结构+模型参数
torch.save(vgg16, "../save/vgg16_method1.pth")

# 保存方式2 ， 保存模型参数
torch.save(vgg16.state_dict(), "../save/vgg16_method2.pth")

