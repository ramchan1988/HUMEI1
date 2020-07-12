"""
测试 asyncio 异步

"""
import time
from concurrent.futures import ThreadPoolExecutor
import asyncio

async def pre(d):
    print('d',d)
    time.sleep(1)
    return d

async def pre1(d):
    print('d1',d)
    #time.sleep(1)
    return d

loop=asyncio.get_event_loop()

if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete( asyncio.wait( [pre(d) for d in range(10)] ))

    loop.run_until_complete( asyncio.wait( [pre1(d) for d in range(10)] ))


    loop.close()












