import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

test_data = torchvision.datasets.CIFAR10("./dataset", train=False, transform=torchvision.transforms.ToTensor())
test_loader = DataLoader(dataset=test_data, batch_size=4, shuffle=False, num_workers=0, drop_last=False)

# 测试
img, target = test_data[0]
# img.shape:则表示取彩色图片的长、宽、通道。
print(img.shape)
print(target)


writer = SummaryWriter("../dataloader")
# step = 0
# for data in test_loader:
#     imgs, targets = data
#     # print(imgs.shape)
#     # print(targets)
#     writer.add_images("test_data",imgs,step)
#     step += 1

for epoch in range(2):
    step = 0
    for data in test_loader:
        imgs, targets = data
        writer.add_images("Epoch:{}".format(epoch),imgs,step)
        step += 1

writer.close()