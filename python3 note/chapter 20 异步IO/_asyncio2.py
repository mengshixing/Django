#我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：

import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s' % host)
    
    connect =asyncio.open_connection(host,80)
    
    reader,writer=yield from connect
    
    header='GET / HTTP/1.0\r\nHost:%s\r\n\r\n' % host
    
    writer.write(header.encode('utf-8'))
    
    #https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter
    #写操作清空缓冲区是一个协程
    yield from writer.drain()
    
    while True:
        line = yield from reader.readline()
        
        #加上测试并发
        yield from asyncio.sleep(1)
        if line == b'\r\n':
            break
        
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    
    
    # 关闭连接
    
    writer.close()
    
    
loop=asyncio.get_event_loop()

task=[wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]

loop.run_until_complete(asyncio.wait(task))

loop.close()
    
    
    
# wget www.163.com
# wget www.sohu.com
# wget www.sina.com.cn
# www.163.com header > HTTP/1.0 302 Moved Temporarily
# www.sohu.com header > HTTP/1.1 200 OK
# www.sina.com.cn header > HTTP/1.1 200 OK
# www.163.com header > Server: Cdn Cache Server V2.0
# www.sohu.com header > Content-Type: text/html;charset=UTF-8
# www.sina.com.cn header > Server: nginx
# www.163.com header > Date: Tue, 18 Jul 2017 10:07:10 GMT
# www.sohu.com header > Connection: close
# www.sina.com.cn header > Date: Tue, 18 Jul 2017 10:07:10 GMT
# www.163.com header > Content-Length: 0
# www.sohu.com header > Server: nginx
# www.sina.com.cn header > Content-Type: text/html
# www.163.com header > Location: http://www.163.com/special/0077jt/error_isp.html
# www.sohu.com header > Date: Tue, 18 Jul 2017 10:07:00 GMT
# www.sina.com.cn header > Content-Length: 597580
# www.163.com header > Connection: close
# www.sohu.com header > Cache-Control: max-age=60
# www.sina.com.cn header > Connection: close
# www.sohu.com header > X-From-Sohu: X-SRC-Cached
# www.sina.com.cn header > Last-Modified: Tue, 18 Jul 2017 10:04:52 GMT
# www.sohu.com header > Content-Encoding: gzip
# www.sina.com.cn header > Vary: Accept-Encoding
# www.sohu.com header > FSS-Cache: HIT from 7218290.12723324.8272070
# www.sina.com.cn header > Expires: Tue, 18 Jul 2017 10:07:49 GMT
# www.sohu.com header > FSS-Proxy: Powered by 6301029.10888559.7355051
# www.sina.com.cn header > Cache-Control: max-age=60
# www.sina.com.cn header > X-Powered-By: shci_v1.03
# www.sina.com.cn header > Age: 22
# www.sina.com.cn header > Via: http/1.1 cnc.beixian.ha2ts4.205 (ApacheTrafficServer/4.2.1.1 [cMsSfW]),
# http/1.1 cnc.qingdao.ha2ts4.103 (ApacheTrafficServer/4.2.1.1 [cHs f ]), http/1.1 
    # cnc.tianjin.ha2ts4.711 (ApacheTrafficServer/4.2.1.1 [cHs f ])
# www.sina.com.cn header > X-Cache: MISS.205
# www.sina.com.cn header > X-Via-CDN: f=edge,s=cnc.tianjin.ha2ts4.755.nb.sinaedge.com,
    # c=111.160.189.62;f=Edge,s=cnc.tianjin.ha2ts4.711,c=125.39.59.75;f=edge,
    # s=cnc.qingdao.ha2ts4.105.nb.sinaedge.com,c=125.39.59.71;f=Edge,s=cnc.qingdao.ha2ts4.103,c=125.39.59.71;
    # f=edge,s=cnc.beixian.ha2ts4.205.nb.sinaedge.com,c=27.221.16.103;f=Edge,s=cnc.beixian.ha2ts4.205,c=61.158.251.196
# www.sina.com.cn header > X-Cache: HIT.103
# www.sina.com.cn header > X-Cache: HIT.71  
    
    
    
    
    
# writer.drain  

# 内存总线在同一时刻只能服务写操作或者读操作中的一种，这是因为总线只能以一个方向驱动。

# 之前的内存控制器将写缓冲在一个写队列中来允许读请求充分利用内存总吸纳，当写队列满时，或者达到某一个水位，
# 内存调度其就或切换到write drain模式，这时它清空写队列【可能完全清空，也可能清空到某个程度】 
# 在这个write drain的过程中，内存总线只能服务写操作，另外，切换进入或者离开write drain模式会对DRAM协议造成一定开销，
# 这叫做(called read-to-write and write-to-read turnaround delays, tRTW and tWTR, 
# approximately 7.5ns and 15ns, respectively [A case for exploiting subarray-level parallelism (SALP) in DRAM] )

# 在这个过程中读写操作都不能调度使用总吸纳，造成浪费珍贵的总线资源，所以频繁的切换到write drain模式，
# 或者在write drain模式中很长时间会对读操作造成很大的开销，这对于读密集的应用以及整个系统的性能影响很大。
