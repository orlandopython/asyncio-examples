import asyncio

async def sleeper(val: int):
    print('Sleeping', val)
    await asyncio.sleep(val)
    print('Done', val)
    return val

loop = asyncio.get_event_loop()
coros = [sleeper(i) for i in range(3)]
result = loop.run_until_complete(asyncio.gather(*coros))
print(result)
