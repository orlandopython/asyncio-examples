import asyncio, aiohttp

async def fetch_item(tag: int) -> dict:
    """Returns response for a single tag"""
    url = f'https://httpbin.org/json'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

def get_all_data(loop, tags: [int]) -> [dict]:
    """Returns responses for all tags"""
    coroutines = [fetch_item(tag) for tag in tags]
    return loop.run_until_complete(asyncio.gather(*coroutines))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(get_all_data(loop, list(range(1000))))
