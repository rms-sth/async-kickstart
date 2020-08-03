import asyncio
from asyncio.tasks import sleep

async def main(f: asyncio.Future):
    await asyncio.sleep(1)
    f.set_result('I have finished')


loop = asyncio.get_event_loop()
fut = asyncio.Future()
print(fut.done())

loop.create_task(main(fut))
# print(loop.create_task(main(fut)))
# <Task pending name='Task-1' coro=<main() running at future_example1.py:4>>

loop.run_until_complete(fut)
print(fut.done())

print(fut.result())