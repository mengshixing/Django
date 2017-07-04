#除了内建模块,还有许多第三方模块

#基本上，所有的第三方模块都会在PyPI - the Python Package Index上注册，
#只要找到对应的模块名字，即可用pip安装。

#PIL模块 Python Imaging Library支持到Python 2.7,Pillow，支持最新Python 3.x

from PIL import Image

im=Image.open('ico.png')
print(im.size)#(227, 370)
x,y=im.size
#缩放一半
im.thumbnail((x//2,y//2))
#保存
im.save('_testico.png','png')

#还有切片、旋转、滤镜、输出文字、调色板等功能
#模糊效果

from PIL import ImageFilter

#模糊滤镜 ImageFilter
im1=im.filter(ImageFilter.BLUR)
#保存,此时是在压缩一半的基础上进行模糊
im1.save('_testico1.png','png')

#ImageDraw提供了一系列绘图的方法

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#随机字母
def random_char():
    return chr(random.randint(65,90))

#随机颜色
#rgb (0,0,0)是黑色(255,255,255)是白色 数字越大越浅色
def random_color1():
    return (random.randint(64, 255),random.randint(64, 255),random.randint(64, 255))
def random_color2():
    return (random.randint(32, 127),random.randint(32, 127),random.randint(32, 127))
        
#返回一个随机tuple        
def line():
    return (random.random()*240,random.random()*60,random.random()*240,random.random()*60)
width=240
height=60   
 
#初始化图片 
_im=Image.new('RGB',(width,height),(255,255,255))

#设置字体,我下载了字体放在文件夹中
font=ImageFont.truetype('bb2117/Arial.ttf',36)

#绘画对象
draw=ImageDraw.Draw(_im)

#图片每个元素进行填充
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=random_color1())

#写入4个字母
# Position是一个二元元组，指定字符串左上角坐标，string是要写入的字符串
# options选项可以为fill或者font(只能选择其中之一作为第三参量，
# 不能两个同同时存在，要改变字体颜色，见ImageFont模块中的NOTE)。
# 其中fill指定字的颜色，font指定字体与字的尺寸，
# font必须为ImageFont中指定的font类型，具体用法见ImageFont.Truetype()  
for i in range(4):
    #倾斜写法
    img1=Image.new('RGBA',(55,55),(255,255,255,0))#新建一个透明图片img1
    img_font=ImageDraw.Draw(img1)#img1作为画板
    img_font.text((15,8),random_char(),font=font,fill=random_color2())#img1上写字
    img1=img1.rotate(random.randint(-30,30))#img1旋转
    _im.paste(img1,(10+i*60,10),mask=img1)#把img1粘贴到img上面

    #正常写法
    #draw.text((60*i+10,10),random_char(),font=font,fill=random_color2())
    draw.line(line(),random_color2())#添加干扰杂线
_im.save('identcode.png','png')













    
