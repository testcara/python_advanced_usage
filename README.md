## Python多线程
### 创建多线程
python中有两个模块（_thread和threading）支持多线程的创建， threading是高级模块，是对基本模块（_thread）的封装。一般我们使用threading来创建多线程。
```
import threading, time                                                                                                                                                        

def loop():
    print("Thread %s is running..." % threading.current_thread().name)
   n = 0 
while n < 5:
   n = n + 1 
       print('thread %s is writing >>> %s' % (threading.current_thread().name, n)) 
            time.sleep(1)
   print('thread %s is ended ...' % threading.current_thread().name)


print("Thread %s is running..." % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s is ended ...' % threading.current_thread().name)
```
输出为：
```
Press ENTER or type command to continue
Thread MainThread is running...
Thread LoopThread is running...
thread LoopThread is writing >>> 1
thread LoopThread is writing >>> 2
thread LoopThread is writing >>> 3
thread LoopThread is writing >>> 4
thread LoopThread is writing >>> 5
thread LoopThread is ended ...
thread MainThread is ended ...

```
### 线程锁
程序最小的独立资源单元是以进程为单位的，即是进程之间，资源相互独立，线程之间，资源（变量和代码块等）相互共享。
进程中的任何一个变量可以被任何一个线程所修改，于是可能出现多个线程同时修改一个变量，然后把内容给改乱的情况。
如下：
```
import time
import threading

data = 1000

def change_value(n):
  global data
  data = data + n 
  data = data - n 
  
def thread_function(n):
  for i in range(1000000):                                                                                                                                                                            
      change_value(n)  
  
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
```
输出结果为：
```
Press ENTER or type command to continue
Thread MainThread has started ...
1020
```
我们看到结果并不是1000，这是因为：
* 多线程间共享进程变量，任何一个进程都可以修改变量
* 线程之间交替执行，且执行顺序由操作系统决定。
* 即时是简单的加减法，但对于高级语言，仍然是需要多步完成。即：
```
a = a + 1
```
实际上的执行操作为：
```
x = a + 1
a = x
```
让我们假想当执行到 x= a + 1操作系统切换了线程，则就会出现上案例中出现的问题。
为了避免这种现象，我们可以使用资源锁。锁只有一个，只有当前线程执行完成，释放资源锁，
其他线程才能执行。资源锁不释放时，即时操作系统切换线程，但是由于资源被占用，则会
线程会被挂起，返回继续当前线程，继续执行。则我们尝试用锁来进行执行：
```
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
```
则执行结果为：
```
Press ENTER or type command to continue
Thread MainThread has started ...
1000
```
### 多线程的效率提升
python的多线程是真的线程而非虚拟线程，理论上讲，一个线程会占用一个cpu，而多个线程
会占用多个cpu，而实际上，由于python设计的缺陷，python的多线程无论线程个数，永远都
只有一个在执行，这主要是由于GIL(global interpreter lock)编译器锁的存在。任何线程
在执行前都必须先获取GIL锁，执行完100行代码或者等待资源而被挂起时，释放该锁，其他线程
才会得以执行，从效果上来，效率还是得到了提升。

### 多进程与多线程的比较
多进程和多线程都可以实现效率的提升，但是由于资源共享和锁机制，所以多进程较多线程更稳定。
但无论多进程还是多线程，并不是盲目增加并发数目就能线性增加效率的。如何最好的利用python
提供的功能，实现高效率的多并发，我们会在后面章节中进行详细讲解。
