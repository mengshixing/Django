# @asyncio.coroutine可以把一个generator标记为coroutine类型，
# 然后在coroutine内部用yield from调用另一个coroutine实现异步操作

# async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
    # 把@asyncio.coroutine替换为async；
    # 把yield from替换为await。

import asyncio
async def hello():
    print(1)
    await asyncio.sleep(2)
    print(2)
    
loop=asyncio.get_event_loop()

loop.run_until_complete(asyncio.wait([hello(),hello()]))

loop.close()