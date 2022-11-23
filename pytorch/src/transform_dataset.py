import torchvision

dataset_transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])


train_set = torchvision.datasets.CIFAR10(root="./dataset", transform=dataset_transform, train=True, download=True)
test_set = torchvision.datasets.CIFAR10(root="./datatest",transform=dataset_transform, train=False, download=True)
