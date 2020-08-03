# A coroutine is an object that encapsulates the ability to resume an
# underlying function that has been suspended before completion.


async def f():
    return 123


print(type(f))
# <class 'function'>

import inspect

print(inspect.iscoroutinefunction(f))
# True

coro = f()
print(type(coro))

print(inspect.iscoroutine(coro))
