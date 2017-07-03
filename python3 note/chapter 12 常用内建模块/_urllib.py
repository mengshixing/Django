#urllib提供了一系列用于操作URL的功能。
#GET

from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data=f.read()
    #print(data)
    print(f.status,f.reason)#200 OK
    for k,v in f.getheaders():
        print(k,':',v)
    
    print(data.decode('utf-8'))
# Date : Mon, 03 Jul 2017 09:34:13 GMT
# Content-Type : application/json; charset=utf-8
# Content-Length : 2055
# Connection : close
# Vary : Accept-Encoding
# X-Ratelimit-Remaining2 : 96
# X-Ratelimit-Limit2 : 100
# Expires : Sun, 1 Jan 2006 01:00:00 GMT
# Pragma : no-cache
# Cache-Control : must-revalidate, no-cache, private
# Set-Cookie : bid=Y-YvCkUOI0M; Expires=Tue, 03-Jul-18 09:34:13 GMT; Domain=.douban.com; Path=/
# X-DOUBAN-NEWBID : Y-YvCkUOI0M
# X-DAE-Node : sindar16a
# X-DAE-App : book
# Server : dae
    
#Request对象模拟设备访问

rq=request.Request('https://www.baidu.com/')#抓取百度手机网页
rq.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 \
(KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')#模拟iphone6

with request.urlopen(rq) as f:
    data=f.read()
    #print(data)
    print(f.status,f.reason)#200 OK
    for k,v in f.getheaders():
        print(k,':',v)
    with open('request.html','a',encoding='utf8',errors='ignore') as f:
        f.write(data.decode('utf-8'))
    
#post 此时data参数需要以bytes方式传入

from urllib import parse
print('login to sina')
email=input('please input email')
password=input('please input password')

login_data=parse.urlencode([
    ('username', email),
    ('password', password),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req=request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin','https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS\
 X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?\
entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#https://zh.wikipedia.org/wiki/HTTP%E5%A4%B4%E5%AD%97%E6%AE%B5
#跨来源资源共享 的请求（要求服务器在回应中加入一个‘访问控制-允许来源’
#（'Access-Control-Allow-Origin'）字段）。

with request.urlopen(req,data=login_data.encode('utf-8')) as f:
    print(f.status,f.reason)
    for k,v in f.getheaders():
        print(k,':',v)
        
    print(f.read().decode('utf-8'))

#练习,利用urllib读取XML，将XML一节的数据由硬编码改为由urllib获取：

from urllib import request,parse
from xml.parsers.expat import ParserCreate

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
    print(_handler.weather)
    
def fetch_xml(url):
    rq=request.Request(url) 
    rq.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 \
    (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')#模拟iphone6
    with request.urlopen(rq) as f:
        data=f.read()
        #print(data)
        print(f.status,f.reason)#200 OK
        for k,v in f.getheaders():
            print(k,':',v)
        #with open('request.html','a',encoding='utf8',errors='ignore') as f:
            #f.write(data.decode('utf-8'))
        parse_weather(data.decode('utf-8'))

        

    

    
fetch_xml('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from\
%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)\
%20where%20text%3D%22beijing%2C%20china%22)%20and%20u%3D%27c%27%20&format=xml\
&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeysw%2C%20scotland%22)%20and\
%20u%3D%27c%27%20&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')





# Handler

# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：

# proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# with opener.open('http://www.example.com/login.html') as f:
    # pass







