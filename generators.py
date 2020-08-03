def g():
    yield 123


print(type(g))
# <class 'function'>

gen = g()
print(type(gen))
# <class 'generator'>

# Even though g is sometimes incorrectly referred to as a “generator,” it remains a
# function, and it is only when this function is evaluated that the generator is
# returned. Coroutine functions work in exactly the same way: you need to call the
# async def function to obtain the coroutine object.
