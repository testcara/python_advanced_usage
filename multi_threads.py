import threading, time

def loop():
    print("Thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s is writing >>> %s' %
              (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s is ended ...' % threading.current_thread().name)


print("Thread %s is running..." % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s is ended ...' % threading.current_thread().name)
