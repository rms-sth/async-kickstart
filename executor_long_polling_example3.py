import asyncio
import time


async def make_coro(future):
    try:
        return await future
    except asyncio.CancelledError:
        return await future


async def main():
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, blocking)
    asyncio.current_task(make_coro(future))
    print(f"{time.ctime()} Hello...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} Goodbye...")


def blocking():
    time.sleep(2.0)
    print(f"{time.ctime()} Hello from a thread...")


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Bye!")

