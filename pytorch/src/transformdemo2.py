from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import  transforms
# 用PIL打开一个图像
img_path = "../data/train/ants_image/6240329_72c01e663e.jpg"
img = Image.open(img_path)

# tensorboard创建
writer = SummaryWriter("../logs")

# PIL Image -> tensor
# ToTensor
tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)
writer.add_image("tensor_img", tensor_img)

# Normalize 归一化
print(tensor_img[0][0][0])
trans_norm = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
img_norm = trans_norm(tensor_img)
print(img_norm[0][0][0])

# Resize
print(img.size)
trans_resize = transforms.Resize((512, 512))
# img PIL -> resize -> img_resize PIL
img_resize = trans_resize(img)
# img_resize PIL -> totensor -> img_resize totensor
img_resize_totentor = tensor_trans(img_resize)
writer.add_image("Resize", img_resize_totentor, 0)
print(img_resize_totentor)

# Compose - resize - 2
trans_resize_2 = transforms.Resize(512)
# PIL -> resize PIL -> tensor
trans_compose = transforms.Compose([trans_resize_2, tensor_trans])
img_resize2 = trans_compose(img)
writer.add_image("Resize", img_resize2)

# RandomCrop

trans_random = transforms.RandomCrop(512)
trans_compose2 = transforms.Compose([trans_random, tensor_trans])
for i in range(10):
    img_crop = trans_compose2(img)
    writer.add_image("RandomCrop", img_crop)

writer.close()