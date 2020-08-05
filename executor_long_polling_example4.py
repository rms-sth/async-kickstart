import asyncio
import time
from concurrent.futures import ThreadPoolExecutor as Executor


async def main():
    print(f"{time.ctime()} Hello...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} Goodbye...")
    loop.stop()


def blocking():
    time.sleep(2)
    print(f"{time.ctime()} Hello from a thread!")


loop = asyncio.get_event_loop()
executor = Executor()
loop.set_default_executor(executor)
loop.create_task(main())
future = loop.run_in_executor(None, blocking)

try:
    loop.run_forever()
except KeyboardInterrupt:
    print("Cancelled...")

tasks = asyncio.all_tasks(loop=loop)
for t in tasks:
    t.cancel()

group = asyncio.gather(*tasks, return_exceptions=True)
loop.run_until_complete(group)

executor.shutdown(wait=True)
loop.close()

# Thu Aug  6 01:53:29 2020 Hello...
# ^CCancelled...
# Thu Aug  6 01:53:31 2020 Hello from a thread!
