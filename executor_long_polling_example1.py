import asyncio
import time


async def main():
    loop = asyncio.get_running_loop()
    loop.run_in_executor(
        None, blocking
    )  # run_in_executor() does not create a Task instance: it returns a Future.
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1)
    print(f"{time.ctime()} Goodbye!")


def blocking():
    time.sleep(1.5)
    print(f"{time.ctime()} Hello from a thread!")


asyncio.run(main())


# when executor jobs take longer to finish than all the pending Task instances.
# The short answer is: without intervention, we’re going to get errors:

#################
# Error:
# exception calling callback for <Future at 0x7f5a9138abb0 state=finished returned NoneType>
# raise RuntimeError('Event loop is closed')
# RuntimeError: Event loop is closed

