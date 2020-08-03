# A coroutine is an object that encapsulates the ability to resume an
# underlying function that has been suspended before completion.


async def f():
    return 123


coro = f()

try:
    coro.send(None)
except StopIteration as e:
    print("The answer is:", e.value)

