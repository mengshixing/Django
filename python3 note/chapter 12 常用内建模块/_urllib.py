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
	
	