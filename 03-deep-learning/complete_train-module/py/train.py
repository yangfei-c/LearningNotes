#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/12 16:44
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : train.py
# @Software: PyCharm

import torchvision
from torch.utils.data import DataLoader

#准备数据集
train_data=torchvision.datasets.CIFAR10(root="../dataset",train=True,
                transform=torchvision.transforms.ToTensor(),download=True)
test_data=torchvision.datasets.CIFAR10(root="../dataset",
                train=False,transform=torchvision.transforms.ToTensor(),download=True)

#打印数据集长度
train_data_size=len(train_data)
test_data_size=len(test_data)
print("训练集长度为：{}".format(train_data_size))
print("测试集长度为：{}".format(test_data_size))

#Dataloader加载数据集
train_data_loader=DataLoader(train_data,batch_size=64)
test_data_loader=DataLoader(test_data,batch_size=64)

#搭建神经网络
