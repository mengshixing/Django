#virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。

首先，我们用pip安装virtualenv：

 pip3 install virtualenv

 
 第一步，创建目录：建立一个文件夹
 
 第二步，切换到对应文件夹,创建一个独立的Python运行环境
 
 virtualenv --no-site-packages venv
 
 参数--no-site-packages意思是所有第三方包都不会复制过来
 
 
 进入虚拟环境使用:切换到对应文件夹,source venv/bin/activate 可以进入该环境
 (window 切换目录到venv/Scripts/ 然后执行activate即可)
 
 退出虚拟环境:deactivate即可
 
 
 virtualenv是如何创建“独立”的Python运行环境的呢？
 原理很简单，就是把系统Python复制一份到virtualenv的环境，
 用命令source venv/bin/activate进入一个virtualenv环境时，
 virtualenv会修改相关环境变量，让命令python和pip均指向当前的virtualenv环境。