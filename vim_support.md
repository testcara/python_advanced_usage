### VIM python IDE支持
使用linux我们不能避免会用vim去编辑文件，这些文件有时候可能就是python文件。
在linux环境下，我们可以有各种编辑器，但是最强大的编辑器就是vim, 哈哈哈哈哈哈，当然，前提是你进行适当配置的前提下。

让我来告诉如何在rhel7上如何配置python ide
#### 前提
python和pip已经安装
#### 步骤
1、升级 vim 7 到 vim 8
```
# 查看版本
vim --version
# 使用 install_vim8.sh 去安装vim8, 请确定在进行安装之前，
# 进行脚本内部的操作和参数确认
sudo ./install_vim8.sh
```
2、安装 python 模块
```
pip3 -i requirement.txt --user
```
3、安装.vimrc到你的工作目录下
```
mv .vimrc ~/.vimrc
```
4. 使用 vim 进行 python 程序开发
```
import os
def helloworld(name):
    print("Hello world, {}!".format(name))
helloworld('cara')
```
按下f5则程序会执行，按下enter, 则我们则会的输出结果如下：
```
Press ENTER or type command to continue
Hello world, cara!

real	0m0.050s
user	0m0.039s
sys  	0m0.011s

Press ENTER or type command to continue
```
则表示我们已经配置完成，可以使用vim进行python进行的高效开发了。
