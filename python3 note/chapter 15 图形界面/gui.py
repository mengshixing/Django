#GUI图形界面Python支持多种图形界面的第三方库，包括:Tk,wxWidgets,Qt,GTK
#Python自带的库是支持Tk的Tkinter

# 我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；
# Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
# Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。
# 所以，我们的代码只需要调用Tkinter提供的接口就可以了。

from tkinter import *
class application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)     
        
        # 在GUI中，每个Button、Label、输入框等，都是一个Widget。
        # Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
        # pack()方法把Widget加入到父容器中，并实现布局。
        # pack()是最简单的布局，grid()可以实现更复杂的布局。   
        self.pack()
        
        #创建组件
        self.createWidges()     
    
    #创建标签和按钮
    def createWidges(self):
        self.hellolabel=Label(self,text='hello')
        self.hellolabel.pack()
        
        self.quitbutton=Button(self,text='quit',command=self.quit)#点击执行退出
        self.quitbutton.pack()
        
c=application()
c.master.title='test'#设置标题
c.mainloop()# 主消息循环:

# GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。
# 因此，如果消息处理非常耗时，就需要在新线程中处理。

import tkinter.messagebox as messagebox
class app(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidges()
        
    def createWidges(self):
        #Entry文本框http://www.cnblogs.com/onlyfu/archive/2013/03/07/2947473.html
        self.nameinput=Entry(self)
        self.nameinput.pack()
        
        self.testbutton=Button(self,text='HI',command=self.hello)
        self.testbutton.pack()
        
    def hello(self):
        name=self.nameinput.get() or 'no input' #前者为空时值为no input
        messagebox.showinfo('messageb','hi %s' % name)
    
    
app=app()
app.master.title='test input'
app.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
        
        