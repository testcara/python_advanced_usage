import asyncio
import time


async def main():
    print("[%s] hello" % (time.ctime()))
    await asyncio.sleep(1)
    print("[%s] world!" % (time.ctime()))

asyncio.run(main())
