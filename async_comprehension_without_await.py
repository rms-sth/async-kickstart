import asyncio

async def doubler(n):
    for i in range(n):
        yield i, i*2
        await asyncio.sleep(0.1)

async def main():
    result = [x async for x in doubler(3)]
    print(result)
    # [(0, 0), (1, 2), (2, 4)]

    result = {x:y async for x,y in doubler(3)}
    print(result)
    # {0: 0, 1: 2, 2: 4}

    result = {x async for x in doubler(3)}
    print(result)
    # {(2, 4), (1, 2), (0, 0)}

asyncio.run(main())