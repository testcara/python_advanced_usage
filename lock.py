import time
import threading

data = 1000
lock = threading.Lock()


def change_value(n):
    global data
    data = data + n
    data = data - n


def thread_function(n):
    for i in range(1000000):
        try:
            lock.acquire()
            change_value(n)
        finally:
            lock.release()


print("Thread %s has started ..." % threading.current_thread().name)
thread_1 = threading.Thread(target=thread_function, args=(5,))
thread_2 = threading.Thread(target=thread_function, args=(8,))
thread_3 = threading.Thread(target=thread_function, args=(12,))
thread_4 = threading.Thread(target=thread_function, args=(15,))
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_1.join()
thread_2.join()
thread_3.join()
thread_3.join()
thread_4.join()
print(data)
