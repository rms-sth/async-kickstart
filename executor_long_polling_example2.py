import asyncio
import time


async def main():
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, blocking)

    try:
        print(f"{time.ctime()} Hello")
        await asyncio.sleep(1)
    finally:
        await future


def blocking():
    time.sleep(2)
    print(f"{time.ctime()} Hello from a thread")


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Bye!")

# we must use a try/finally within every single scope where an executor job is created.