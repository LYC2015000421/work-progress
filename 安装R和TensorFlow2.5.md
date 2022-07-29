# Linux服务器下R和TensorFlow的安装

## 在Linux服务器通过conda安装R

在激活的虚拟环境中输入conda install r-base 开始下载

```shell
conda install r-base
```

![image-20220729135031081](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729135031081.png)

Proceed ([y]/n)? 选择y即可。等待安装完毕。

![image-20220729135435436](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729135435436.png)

安装完毕后，输入R就可以进入R了。

![image-20220729140202798](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729140202798.png)

可以看到当前的R的版本是3.6.1，并不是最新版本（最新版本4.2.1）

![image-20220729140252162](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729140252162.png)

R包的安装位置：liuyc@ubuntu:~/anaconda3/envs/test/lib/R$

```shell
liuyc@ubuntu:~/anaconda3/envs/test/lib/R$
```

思考：如何通过conda安装指定版本（低版本）的R包？

查看R的版本 conda search R

![image-20220729140803095](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729140803095.png)

选择下载r3.4.3版本

```shel
conda install r=3.4.3
```

![image-20220729140913283](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729140913283.png)

下载完成后输入R进行测试：

![image-20220729140936082](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729140936082.png)

R的版本是3.4.3，下载成功。

相关链接：

https://blog.csdn.net/qq_61049648/article/details/125565660

https://blog.csdn.net/watermel__/article/details/125315047

## TensorFlow2.5.0安装

Alphafold的Python虚拟环境中需要安装的包如下所示：

![image-20220729190533054](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729190533054.png)

首先，安装tensorflow-cpu==2.5.0

在创建好的Python虚拟环境中输入：

```shell
pip install tensorflow-cpu==2.5.0 -i https://pypi.douban.com/simple/
```

通过豆瓣源进行下载

![image-20220729190747343](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729190747343.png)

下载成功，出现如下提示：

![image-20220729190948606](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729190948606.png)

进入python进行检测

输入如下代码：

```
import tensorflow as tf
tf.__version__
```

显示正确版本，则证明安装成功。

![image-20220729191127468](C:\Users\刘宇辰\AppData\Roaming\Typora\typora-user-images\image-20220729191127468.png)

后续还会进行，其他alphafold相关包的安装。