import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print("%s %s" % (time.ctime(), what))


async def main():
    print(f"started at {time.strftime('%X')}")
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(4, " world!"))

    # wait until the tasks are completed
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
