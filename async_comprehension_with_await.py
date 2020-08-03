import asyncio

async def adder(x):
    await asyncio.sleep(0.1)
    return x + 100


async def factory(n):
    for x in range(n):
        await asyncio.sleep(0.1)
        yield adder, x


async def main():
    results = [await adder(x) async for adder, x in factory(3)]
    print(results)
    # [100, 101, 102]

asyncio.run(main())
