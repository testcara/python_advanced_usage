from multiprocessing import Pool
import os
import time
import random


def test_pool(i):
    print("Run tasks as process ({})".format(os.getpid()))
    start = time.time()
    time.sleep(random.random()*int(i))
    end = time.time()
    print("Tasks %s runs %0.2f seconds." % (os.getpid(), (end-start)))


print("Process({}) started".format(os.getpid()))
p = Pool(4)
for i in range(5):
    p.apply_async(test_pool, args=(i,))
print("Waiting for all sub-processes done ...!")
p.close()
p.join()
print("All tasks completed ...!")
