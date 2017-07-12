http协议简介

	HTML是一种用来定义网页的文本，会HTML，就可以编写网页
	HTTP是在网络上传输HTML的协议，用于浏览器和服务器的通信
	
Request Headers:
	
	GET /his?wd=&from=pc_web&rf=3&hisdata=&json=1&p=3&sid=&req=2&csor=0&cb=jQuery110209345996483358479_1499851492927&_=1499851492928 HTTP/1.1
	Host: www.baidu.com
	Accept:text/html
	Accept-Encoding:gzip, deflate, sdch
	Accept-Language:zh-CN,zh;q=0.8
	Connection:keep-alive
	Cookie:MoodleSession=eagj46ruk3rtrfeqlfl7ge3684
	Host:192.168.0.216
	Referer:http://192.168.0.216/vod/web/index.php?r=home/sspace/space&courseid=34
	User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
	X-Requested-With:XMLHttpRequest
	
	Host:域名
	GET /    HTTP/1.1
	GET表示一个读取请求，将从服务器获得网页数据，
	/表示URL的路径，URL总是以/开头，/就表示首页，
	最后的HTTP/1.1指示采用的HTTP协议版本是1.1。目前HTTP协议的版本就是1.1，
	但是大部分服务器也支持1.0版本，主要区别在于1.1版本允许多个HTTP请求复用一个TCP连接，以加快传输速度。

Response Headers:
	
	HTTP/1.1 200 OK
	Cache-Control: private
	Connection: Keep-Alive
	Content-Length: 95
	Content-Type: baiduApp/json; v6.27.2.14; charset=UTF-8
	Date: Wed, 12 Jul 2017 09:24:42 GMT
	Expires: Wed, 12 Jul 2017 10:24:42 GMT
	Server: suggestion.baidu.zbb.df

	200 OK:
	200表示一个成功的响应，后面的OK是说明。失败的响应有404 Not Found：
	网页不存在，500 Internal Server Error：服务器内部出错，等等。
	
	Content-Type: text/html:
	text/html表示HTML网页。请注意，浏览器就是依靠Content-Type来判断响应的内容是网页还是图片，
	是视频还是音乐。浏览器并不靠URL来判断响应的内容，所以，即使URL是http://example.com/abc.jpg，它也不一定就是图片。
	
	
当浏览器读取到新浪首页的HTML源码后，它会解析HTML，显示页面，然后，根据HTML里面的各种链接，
再发送HTTP请求给新浪服务器，拿到相应的图片、视频、Flash、JavaScript脚本、CSS等各种资源，
最终显示出一个完整的页面。所以我们在Network下面能看到很多额外的HTTP请求。
	
HTTP请求:

	步骤1:浏览器首先向服务器发送HTTP请求，请求包括：方法：GET还是POST，GET仅请求资源，POST会附带用户数据；
		路径：/full/url/path；域名：由Host头指定：Host: www.sina.com.cn以及其他相关的Header；
		如果是POST，那么请求还包括一个Body，包含用户数据。
	
	步骤2:服务器向浏览器返回HTTP响应，响应包括：响应代码：200表示成功，3xx表示重定向，
		4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；
		响应类型：由Content-Type指定；以及其他相关的Header；
		通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容，网页的HTML源码就在Body中。
	
	步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。
	
HTTP格式:
	
	一个HTTP包含Header和Body两部分，其中Body是可选的.
	
	HTTP GET请求的格式：
		GET /path HTTP/1.1
		Header1: Value1
		Header2: Value2
		Header3: Value3

	每个Header一行一个，换行符是\r\n。当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。
	
	HTTP响应的格式：
		200 OK
		Header1: Value1
		Header2: Value2
		Header3: Value3
	
	HTTP响应如果包含body，也是通过\r\n\r\n来分隔的。请再次注意，Body的数据类型由Content-Type头来确定，
	如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据。
	当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip，
	所以，看到Content-Encoding: gzip时，需要将Body数据先解压缩，才能得到真正的数据。
	压缩的目的在于减少Body的大小，加快网络传输。
	
	
	
	
	
	
	
	
	