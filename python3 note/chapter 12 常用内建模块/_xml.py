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
    <div>
        <li><a href="ruby">Ruby</a></li>
    </div>
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
# char_data

# char_data
# start_element li {}
# start_element a {'href': 'python'}
# char_data Python
# end_element a
# end_element li
# char_data

# char_data
# start_element div {}
# char_data

# char_data
# start_element li {}
# start_element a {'href': 'ruby'}
# char_data Ruby
# end_element a
# end_element li
# char_data

# char_data
# end_element div
# char_data

# end_element div 结束div

#练习解析雅虎天气
data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''

class defaultParseXML():
    def __init__(self):
        self.weather={}
        self.count=0
    def start_element(self,name,attrs):
        if name=='yweather:location' or name=='yweather:astronomy':
            self.weather.update(attrs)
        if name=='yweather:forecast':
            self.count=self.count+1
            if self.count==1:
                self.weather['today']=attrs
            if self.count==2:
                self.weather['tomorrow']=attrs
    def end_element(self,name):
        pass
    
    def char_data(self,text):#可以给类加current属性,在start里面赋值,这里写入对应值
        pass
        
        
        
        
def parse_weather(data):

    _handler=defaultParseXML()

    parser=ParserCreate()
    parser.StartElementHandler = _handler.start_element
    parser.EndElementHandler = _handler.end_element
    parser.CharacterDataHandler = _handler.char_data
    parser.Parse(data)
    
    print (_handler.weather)

weather = parse_weather(data)

