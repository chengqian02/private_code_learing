from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np



writer = SummaryWriter("../logs")


image_path = "../data/train/ants_image/0013035.jpg"
image_path2 = "data/train/ants_image/5650366_e22b7e1065.jpg"
img = Image.open(image_path)
img2 = Image.open(image_path2)
img_array = np.array(img)
img_array2 = np.array(img2)

print(type(img_array))
print(img_array.shape)
writer.add_image("test", img_array, 1, dataformats='HWC')
writer.add_image("test", img_array2, 2, dataformats='HWC')
# writer.add_image()
# y = x
for i in range(100):
    writer.add_scalar("y=2x", 2*i ,i)

writer.close()