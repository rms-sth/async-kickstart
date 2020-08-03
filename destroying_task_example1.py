import asyncio


async def f(delay):
    await asyncio.sleep(delay)


loop = asyncio.get_event_loop()

t1 = loop.create_task(f(1))
t2 = loop.create_task(f(2))

loop.run_until_complete(t1)
loop.close()

# Task was destroyed but it is pending!
# task: <Task pending name='Task-2' coro=<f() running at destroying_task_example1.py:5> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x7f8e2e4fb8b0>()]>>
