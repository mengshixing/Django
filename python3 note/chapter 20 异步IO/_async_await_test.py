#test
#我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：

import asyncio

async def wget(host):
    print('wget %s' % host)
    
    connect =asyncio.open_connection(host,80)
    
    reader,writer=await connect
    
    header='GET / HTTP/1.0\r\nHost:%s\r\n\r\n' % host
    
    writer.write(header.encode('utf-8'))
    
    #https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter
    #写操作清空缓冲区是一个协程
    await writer.drain()
    
    while True:
        line = await reader.readline()
        
        #加上测试并发
        await asyncio.sleep(1)
        if line == b'\r\n':
            break
        
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    
    
    # 关闭连接
    
    writer.close()
    
    
loop=asyncio.get_event_loop()

task=[wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]

loop.run_until_complete(asyncio.wait(task))

loop.close()