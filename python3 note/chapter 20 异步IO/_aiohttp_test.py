# 如果把asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，
# 因此可以用单线程+coroutine实现多用户的高并发支持。
# asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。

import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(2)
    
    return web.Response(body=b'<h1>Idex</h1>',content_type='text/html')
    
async def hello(request):  
    await asyncio.sleep(2)
    
    text='<h1>welcome %s </h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'),content_type='text/html')

#init()是一个coroutine 
async def init(loop):
    
    app=web.Application(loop=loop)
    
    app.router.add_route('GET','/', index)
    
    app.router.add_route('GET','/hello/{name}', hello)
    
    #loop.create_server()则利用asyncio创建TCP服务。
    srv=await loop.create_server(app.make_handler(),'192.168.0.124',5000)
    
    print(1)
    
    return srv
    
loop=asyncio.get_event_loop()

loop.run_until_complete(init(loop))

loop.run_forever()