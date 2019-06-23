import asyncio


async def test1():
    print("--> [test1] 1 ...")
    await asyncio.sleep(1)
    print("--> [test1] 2 ...")
    await asyncio.sleep(1)
    print("--> [test1] 3 ...")


async def test2():
    print("--> [test2] 1 ...")
    print("--> [test2] 2 ...")
    print("--> [test2] 3 ...")

a = test1()
b = test2()

try:
    a.send(None)
except StopIteration:
    pass

try:
    b.send(None)
except StopIteration:
    pass
