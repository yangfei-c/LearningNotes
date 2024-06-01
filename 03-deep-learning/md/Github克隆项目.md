### 项目导入

##### 从github克隆到本地

```sh
git clone https://github.com/facefusion/facefusion.git
```

##### 创建虚拟环境

```sh
conda create -n facefu python=3.10
```

##### 虚拟环境查看

```sh
conda env list 
```

##### 虚拟环境激活

```sh
activate ff
```

##### 虚拟环境删除

```sh
conda remove --name 
```

##### pycharm虚拟环境显示

```
F:\Tools\anaconda3\condabin\conda.bat
选中这个然后点击 Load Environments就会显示创建出的虚拟环境了
然后重启pycharm前面就会出现创建的虚拟环境ff了
```

![image-20240501225550968](C:\Users\acer\AppData\Roaming\Typora\typora-user-images\image-20240501225550968.png)

### 安装依赖包

##### 基于requirements.txt安装

```sh
pip install -r requirements.txt
```

###### 错误1

```
ERROR: pip's dependency resolver does not currently take into account all the packages that are 
installed. This behaviour is the source of the following dependency conflicts.
dailycheckin 24.1.20 requires requests~=2.25.1, but you have requests 2.31.0 which is incompatib
le. 表明依赖之间出现问题
```

###### 检查依赖关系

```sh
In：pip check
Out：dailycheckin 24.1.20 has requirement requests~=2.25.1, but you have requests 2.31.0.
```

###### 解决问题

```sh
pip install "requests<=2.25.1"
#将 requests 降级到一个与 dailycheckin 兼容的版本
```

### 项目部署

##### 开放端口

###### 防火墙

```sh
firewall-cmd --state#查看状态
systemctl start firewalld#开启防火墙
firewall-cmd --zone=public --add-port=4321/tcp --permanent#启动(4321)端口是否
firewall-cmd --reload#重启防火墙
#查看某(4321)端口是否可访问
firewall-cmd --zone=public --query-port=4321/tcp
firewall-cmd --zone=public --list-port
systemctl stop firewalld.service#关闭防火墙
systemctl stop firewalld.service #停止firewall
```

##### 端口占用

```sh
# 找出占用端口7000的进程ID
sudo netstat -tulpn | grep :7000

# 杀死进程ID（假设这里是1234）
sudo kill -9 1234
```

