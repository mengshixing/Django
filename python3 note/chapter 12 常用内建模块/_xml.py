# 操作XML可以用DOM和SAX

# DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

#python使用SAX需要准备3个事件

# 解析<a href="/">python</a>时
# start_element,在读取<a href="/">时
# char_data,在读取python时
# end_element,在读取</a>时

from xml.parsers.expat import ParserCreate

class defaultSaxHandler():
    def start_element(self,name,attrs):
        print('start_element',name,attrs)
        
    def end_element(self,name):
        print('end_element',name)
    
    def char_data(self,text):
        print('char_data',text)
        
xml1=r'''<?xml version="1.0"?>
<div>
    <li><a href="python">Python</a></li>
    <li><a href="ruby">Ruby</a></li>
</div>
'''

handler=defaultSaxHandler()#初始化一个类实例

parser=ParserCreate()#引入ParserCreate模块
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml1)

# 输出
# start_element div {} 开始div
# char_data 读div内容

# char_data
# start_element li {}
# start_element a {'href': 'python'}
# char_data Python
# end_element a
# end_element li
# char_data

# char_data
# start_element li {}
# start_element a {'href': 'ruby'}
# char_data Ruby
# end_element a
# end_element li
# char_data

# end_element div 结束div

