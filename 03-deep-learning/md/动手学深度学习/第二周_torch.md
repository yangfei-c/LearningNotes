# 动手学深度学习9.16~9.22

## softmax网络架构

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/softmax%E7%BD%91%E7%BB%9C%E6%9E%B6%E6%9E%84.png" style="zoom: 20%;" />

```
与线性回归一样，softmax也是一个单层神经网络，每个输出o1，o2，o3取决于所有输入x1，x2，x3，x4，因此softmax回归的输出层也是全连接层。
```

## 交叉熵损失

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/%E4%BA%A4%E5%8F%89%E7%86%B5%E6%8D%9F%E5%A4%B1.jpg" style="zoom: 33%;" />

## softmax运算

我们并不能将未规范化的预测o直接作为感兴趣的输出，

1.输出数值总和没有限制为1

2.输出可能为负值

```
解决办法
对每个未规范的预测求幂确保输出为非负值
再让每个求幂后的结果除以结果的总和确保输出概率综合为1
```

## 多层感知机

单层感知机只能处理线性可分问题，所有就需要到了多层感知机来处理更多复杂的非线性的问题

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/%E5%8D%95%E9%9A%90%E8%97%8F%E5%B1%82%E5%A4%9A%E5%B1%82%E6%84%9F%E7%9F%A5%E6%9C%BA.png" style="zoom: 25%;" />

```
把前L-1层看作表示，最后一层看作线性预测器
前L-1层负责从输入数据中提取特征或进行特征变换即构建数据的表示
第L层即最后一层，根据提取的特征进行线性预测
隐藏层通过激活函数对输入进行非线性变换，这是层感知机（MLP）等神经网络能够处理复杂的、非线性问题的关键。激活函数的引入使得网络的表示能力大大增强。如果没有激活函数，网络的每一层只能执行线性变换，
```

## 常用激活函数

### ReLU函数

修正线性单元（rectified linear unit,ReLU），实现简单，在各种预测任务中表现良好
$$
ReLU(x)=max(x,0)
$$
如下图所示为ReLU函数及其导数的曲线图

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/ReLU%E5%8F%8A%E5%85%B6%E5%AF%BC%E6%95%B0.png" style="zoom: 50%;" />

### sigmoid函数

又被称为挤压函数，它将范围（-inf,inf）上的任意输入压缩到区间（0，1）上的某个值
$$
sigmoid(x)=\frac{1}{1+e^{-x}}
$$
在隐藏层使用较少被更简单更容易训练的ReLU取代

如下图所示为sigmoid函数及其导数的曲线图

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/sigmoid%E5%8F%8A%E5%85%B6%E5%AF%BC%E6%95%B0.png" style="zoom:33%;" />

### tanh函数

与sigmoid函数类似也能将输入压缩转换到区间（-1，1）上

如下是tanh函数公式
$$
tanh(x)=\frac{1-e^{-2x}} {1+e^{-2x}}
$$
tanh函数关于坐标系原点中心对称

tanh函数及其导数曲线图如下图所示

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/tanh%E5%8F%8A%E5%85%B6%E5%AF%BC%E6%95%B0.png" style="zoom: 33%;" />
