http://www.cnblogs.com/chusiping/archive/2011/11/10/2243805.html
yum -y install wget 安装wget



http://blog.csdn.net/liuweiyuxiang/article/details/52745584 

 1、下载python3.5

wget https://www.Python.org/ftp/python/3.5.0/Python-3.5.0.tgz

注：如果在Linux中下载较慢，可以在Windows操作系统中去Python官网下载：https://www.python.org/downloads/release/python-350/

注意要下载Gzipped source tarball版本的，然后使用WinSCP将下载好的文件Python-3.5.0.tgz拖拽到Linux中，后续步骤还是不变的。

2、解压

tar zxvf Python-3.5.0.tgz

3、进入Python-3.5.0文件夹

cd Python-3.5.0

4、配置安装位置

./configure --prefix=/usr/local/python3.5

注：如果没有安装C语言编译器会提示错误。configure: error: no acceptable C compiler found in $PATH

如果出现错误，在联网的情况下使用 yum install gcc 命令安装gcc编译器

5、编译

make
	make，仅编译；
	make install，编译并安装（比如安装到/usr/bin目录下，然后可以直接使用。
	因为/usr/bin只有管理员才能向里面添加文件，所以通常要加sudo）
	这个要看你的Makefile的,约定俗成的而已，一般"潜规则"
	make就是make all,编译用的,具体编译了那些文件要看你的Makefile
	make install就是把编译出来的二进制文件,库,配置文件等等放到相应目录下
	make clean清除编译结果
	具体的东西都在Makefile里面,只不过大部分应用程序的Makefile都是由configure脚本自动生成的,
	所以Makefile内容都差不多
	http://www.cnblogs.com/hnrainll/archive/2011/06/08/2075052.html
6、安装

make install

7、下载并安装setuptools 18.5

wget https://bootstrap.pypa.io/ez_setup.py -O - | python

注：如果提示错误 --no-check-certificate 

在wget后加上 --no-check-certificate :wget --no-check-certificate https://bootstrap.pypa.io/ez_setup.py -O - | python

8、备份原有python命令执行文件

mv /usr/bin/python /usr/bin/pythonbak

9、创建新python软连接

ln -s /usr/local/python3.5/bin/python3.5 /usr/bin/python

10、查看python版本

python
[plain] view plain copy

    [root@localhost Python-3.5.0]# python  
    Python 3.5.0 (default, Oct  7 2016, 04:34:35)   
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-17)] on linux  
    Type "help", "copyright", "credits" or "license" for more information.  

11、修改yum配置文件
vim /usr/bin/yum 


http://www.cnblogs.com/lifuhei/p/5948074.html

