#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/16 16:19
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : sequence.py
# @Software: PyCharm
import torch
from d2l import torch as d2l
from torch import nn

T=1000
time=torch.arange(1,T+1,dtype=torch.float32)
x=torch.sin(0.01*time)+torch.normal(0,0.2,(T,))
d2l.plot(time,[x],'time','x',xlim=[1,1000],figsize=(6,3))
# plt.show()

tau=4
features=torch.zeros((T-tau,tau))
for i in range(tau):
    features[:,i]=x[i:T-tau+i]
labels=x[tau:].reshape((-1,1))

batchsize,n_train=16,600
train_iter=d2l.load_array((features[:n_train],labels[:n_train]),
                          batchsize,is_train=True)

def init_weights(m):
    if type(m)==nn.Linear(4,10):
        nn.init.xavier_uniform_(m.weight)

def get_net():
    net=nn.Sequential(nn.Linear(4,10),
                      nn.ReLU(),
                      nn.Linear(10,1))
    net.apply(init_weights)
    return net
loss=nn.MSELoss(reduction='none')

def train(net,train_iter,loss,epochs,lr):
    trainer=torch.optim.Adam(net.parameters(),lr)
    for epoch in range(epochs):
        for X,y in train_iter:
            trainer.zero_grad()
            l=loss(net(X),y)
            l.sum().backward()
            trainer.step()
        print(f'epoch{epoch+1},'
              f'loss:{d2l.evaluate_loss(net,train_iter,loss):f}')

net=get_net()
train(net,train_iter,loss,5,0.01)