# Ananconda打包Python环境

Anaconda的Python环境移植，一直是很常用的、实用的功能。conda-pack进行Python环境移植呢一般会在以下情况下使用。

①要在不同的Linux服务器下运行Python程序，然而在另一个Linux服务其中Python的版本和各种包的版本都不相同，因此，需要打包自己的Python环境移植到另一个服务器上。

②自己的Python环境有安装包始终安装不上，但是在别人的Python环境，或者另一个Linux服务器上有，这时，就可以将这个Python环境打包，移植到自己的电脑上。

现在要将home/liuyc/anaconda3/envs中的名为alphafold的python3.7环境打包转移到newdata/liuyc/Alphafold文件夹中。其中，打包的Python环境中有tensorflow2.5.0版本，可以借此检验是否转移成功。

## 1.安装conda-pack

运行以下命令安装conda-pack

```shell
pip install conda-pack
```

![](https://github.com/LYC2015000421/work-progress/blob/master/Pictures/installcondapack.png)

## 2.打包Python环境

选择要打包的Python环境，这里选择alphafold运行如下指令：

```shell
conda pack -n alphafold
```

![](https://github.com/LYC2015000421/work-progress/blob/master/Pictures/movefile.png)

可以看到，在当前的文件位置下，已经出现了alphafold的tar.gz压缩文件，打包已经成功。

## 3.转移Python环境

首先，先将alphafold.tar.gz压缩文件包转移到对应的目录下，newdata/liuyc/Alphafold中。运行Linux中的mv指令。

```shell
sudo mv alphafold.tar.gz /newdata/liuyc/Alphafold
```

![](https://github.com/LYC2015000421/work-progress/blob/master/Pictures/Pythonpack.png)

可以看到，alphafold.tar.gz已经移动到了newdata/liuyc/Alphafold中。进行解压，运行tar指令。

```shell
sudo tar -zxvf apphafold.tar.gz 
```

之后可以看到压缩包已经在当前目录下解压。

![](https://github.com/LYC2015000421/work-progress/blob/master/Pictures/targz.png)

如果是迁移到其他的Linux服务器中，则可以将tar.gz文件解压到对应的anaconda3/envs/文件目录下。

## 相关链接：

https://zhuanlan.zhihu.com/p/452472428

https://blog.csdn.net/ds1302__/article/details/120027173