from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import  transforms

img_path = "../data/train/ants_image/6240329_72c01e663e.jpg"
img = Image.open(img_path)

# tensorboard创建
writer = SummaryWriter("../logs")

# PIL Image -> tensor
tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)

# 把tensor Image 写入transboard
writer.add_image("tensor_img", tensor_img)

writer.close()