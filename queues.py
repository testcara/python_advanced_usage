from multiprocessing import Queue, Process
import os
import time
import random


def write(q):
    print('Write Process: %s ...' % (os.getpid()))
    for value in ['A', 'B', 'C']:
        print('Put %s to queue ...' % (value))
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Read Process: %s ...' % (os.getpid()))
    while True:
        value = q.get(True)
        print('Get %s from queue ...' % (value))


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    pr.terminate()
