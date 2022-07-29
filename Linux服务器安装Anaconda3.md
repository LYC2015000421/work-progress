# Linux服务器中安装Anaconda3

## Anaconda介绍

Anaconda 是一个开源的包、环境管理器，其包含了 conda、Python 等 180 多个科学包及其依赖项，可以用于在同一个机器上安装不同版本的软件包及其依赖，并能够在不同的环境之间切换。

特点：

1、丰富的第三方库

Anaconda 附带了一大批常用数据科学包，它附带了 conda、Python 和 150 多个科学包及其依赖项。因此你可以立即开始处理数据。

2、管理包

Anaconda 是在 conda（一个包管理器和环境管理器）上发展出来的。可以使用 conda 来安装、更新、卸载工具包，并且它更关注于数据科学相关的工具包。在安装 anaconda 时就预先集成了像 Numpy 、 Scipy 、 pandas 、 Scikit-learn 这些在数据分析中常用的包。另外值得一提的是，conda 并不仅仅管理 Python 的工具包，它也能安装非 python 的包。

3、虚拟环境管理

在 conda 中可以建立多个虚拟环境，用于隔离不同项目所需的不同版本的工具包，以防止版本上的冲突。对纠结于 Python 版本的同学们，我们也可以建立 Python2 和 Python3 两个环境，来分别运行不同版本的 Python 代码。

## Anaconda安装包下载至Linux服务器

两种方法：

1.官网（https://repo.anaconda.com/archive/）下载

从官网上下载对应版本对应操作系统的Anaconda安装文件（约500M）。

![image-20220729153051414](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729153051414.png)

通过Xshell的Xftp7进行文件传输

![image-20220729160241852](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729160241852.png)

将需要传输的文件拖拽到服务器中的对应位置进行传输

![image-20220729160300951](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729160300951.png)

传输的过程需要很长的时间，因此不推荐通过Xftp传输大型文件，也不推荐这种安装方法。

2.通过清华镜像进行下载（在服务器中进行）

 清华镜像地址：https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/

举例：

```shell
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.0.1-Linux-x86_64.sh
```

![image-20220729160504102](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729160504102.png)

下载的过程也是非常漫长的（约1h）

当下载完成之后，需要进行安装。

安装过程如下：

运行这两行指令

```shell
chmod +x Anaconda3-5.0.1-Linux-x86_64.sh
./Anaconda3-5.0.1-Linux-x86_64.sh
```

![image-20220729162812300](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729162812300.png)

按enter（回车）继续

![image-20220729162830742](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729162830742.png)

输入yes接受license terms

![image-20220729162846759](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729162846759.png)

点击Enter确定下载位置，

![image-20220729162909894](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729162909894.png)

输入yes，添加环境变量

![image-20220729162929637](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729162929637.png)

提示安装成功

![image-20220729162952327](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729162952327.png)

查看安装内容：

![image-20220729163006882](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729163006882.png)

检测是否安装成功：

```shell
conda -V
```

![image-20220729163306580](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729163306580.png)

显示conda的版本号，证明安装成功。

## Ananconda安装中遇到问题的解决办法

1.显示当前安装的conda信息

```shell
conda info –envs
```

可以看到当前只有一个root的conda环境在/home/liuyc/anaconda3

![image-20220729174904473](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729174904473.png)

2.创建Python环境

```shell
conda create -n test python=3.7 （其中 test是我自己起的名字）
```

![image-20220729174941265](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729174941265.png)

出现的问题：

1.Fetching package metadata ...卡住

![image-20220729175019912](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729175019912.png)

解决方法：https://blog.csdn.net/qq_60143666/article/details/122414931

修改.condarc文件

具体操作：通过vim修改

```shell
vim ~/.condarc
```

将内容修改为：

```shell
ssl_verify: true
show_channel_urls: true
 
channels:
  - http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
```

![image-20220729175150811](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729175150811.png)

之后进行测试：

成功下载文件

![image-20220729175204476](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729175204476.png)

问题2:

出错:

```shell
CondaHTTPError: HTTP 000 CONNECTION FAILED for url
 <https://mirrors.tuna.tsinghua.edu.cn/anaconda/...
```

![image-20220729175238340](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729175238340.png)

解决方法：https://blog.csdn.net/weixin_49304494/article/details/122622134

```shell
vim ~/.condarc
```

```shell
channels:
  - defaults
show_channel_urls: true
default_channels:
  - http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

```

![image-20220729175410941](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729175410941.png)

## Anaconda基本使用

1.显示当前安装的conda信息

```shell
conda info –envs
```

![image-20220729180620283](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729180620283.png)

2.创建虚拟环境

```shell
conda create -n your_env_name python=X.X（3.6、3.7等）
```

3.激活虚拟环境

```shell
source activate your_env_name(虚拟环境名称)
```

![image-20220729183951028](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729183951028.png)

（*号出现在了test上）

4.退出虚拟环境

```shell
source deactivate your_env_name(虚拟环境名称)
```

![image-20220729184225389](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729184225389.png)

（*号回到了root上）

5.安装包

```shell
conda install package_name(包名)
```

以安装tenserflow1.13.1为例

 

请注意：

“=”：在软件包后面加上“=”代表自动安装该软件包制定大版本的最新更新版本，如“tensorflow=1.13”会自动安装tensorflow版本1.13下的最新版本，即“1.13.”小数点后跟最新数字

“==”：在软件包后加上“==”代表安装指定版本软件包，双等号后面版本数字一定要写全，如“tensorflow==1.13.1”就是安装1.13.1版本的tensorflow

 报错：

![image-20220729184638760](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729184638760.png)

解决方法：

网上的解决方法是添加清华源的镜像，但我的已经是清华源镜像了，所以解决方法是把timeout放大，600还是不行，把时间延长到1000.0

```shell
conda config --set remote_read_timeout_secs 1000.0
```

Python第三方库离线安装：（以wandb0.12.21为例）

参考：https://blog.csdn.net/SEU_LL/article/details/119385057

1.首先，在网页https://pypi.org/上寻找正确版本的安装包，找到tar.gz文件进行下载

![image-20220729184733531](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729184733531.png)

通过Xftp将压缩文件发送到服务器指定的位置。

![image-20220729184754640](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729184754640.png)

通过tar -zxvf 进行解压

2.进入到的目录下

![image-20220729184815266](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729184815266.png)

先install

```shell
python setup.py install
```

出现错误提示， 运行pip install –upgrade 进行对应包的升级即可

![image-20220729184855889](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729184855889.png)

出现Finishing processing dependencies for wandb==0.12.21 安装成功

之后，进行build

```shell
python setup.py build
```

![image-20220729184928160](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729184928160.png)

检查是否安装成功

1.通过pip list/conda list 进行查看

![image-20220729184956525](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729184956525.png)

2.输入Python进行编译

import wandb 若没有报错则安装成功

![image-20220729185018252](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729185018252.png)

相关链接：

Anaconda介绍：https://blog.csdn.net/m0_56729179/article/details/124724900

Anaconda下载：https://blog.csdn.net/qq_33290813/article/details/125389669

Anaconda安装：https://blog.csdn.net/wyf2017/article/details/118676765

Fetching package metadata ...卡住解决方法：

https://blog.csdn.net/qq_60143666/article/details/122414931

Anaconda使用: https://blog.csdn.net/a_cherry_blossoms/article/details/123434261