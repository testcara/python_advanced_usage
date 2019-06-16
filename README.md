## Python多进程
在linux中创建进程的方式有以下几种：
* fork()系统调用
* multiprocessing跨平台模块中的Process和Pool
* subprocess模块
让我们分别对这三种方式进行实验和学习
### fork()系统调用
我们使用fork()如下：
```
import os

def test_fork():
  print("Prosess {} started...".format(os.getpid()))
  pid = os.fork()
  print(pid)                                                                                                                                          
  if pid == 0:
      print("I am the child prosess({}) and my parent is {}".format(
          os.getpid(), os.getppid()))
  else:
      print("I({}) just created the child prosess({})".format(os.getpid(),pid))
test_fork()
```
输出结果为：
```
Prosess 29307 started...
29308
I(29307) just created the child prosess(29308)
0
I am the child prosess(29308) and my parent is 29307
```
由上我们可以看出，fork()调用一次，返回两次，先从父进程返回，再从子进程返回。

### multiprocessing的Process和Pool
fork()系统掉用不存在于windows中，跨平台我们可以使用multiprocessing的来实现。我们先常用Process来常见子进程。
```
from multiprocessing import Process
import os

def hello(name):
  print("Hello, {}".format(name))

print("Process({}) started...".format(os.getpid()))
pid = Process(target=hello, args=('cara',))                                                                                                   
print("Child process is alive? {}!".format(pid.is_alive()))
print("Child process({})is starting ..".format(pid.pid))
pid.start()
print("Child process is alive? {}!".format(pid.is_alive()))
pid.join()
print("Child process is alive? {}!".format(pid.is_alive()))
print("Child process({}) has been stopped ..".format(pid.pid))
print("Process({}) completed...".format(os.getpid()))
```
则输出为：
```
Press ENTER or type command to continue
Process(2760) started...
Child process is alive? False!
Child process(None)is starting ..
Child process is alive? True!
Hello, cara
Child process is alive? False!
Child process(2761) has been stopped ..
Process(2760) completed...
```
start后子进程才会激活，并执行，join等待子进程执行完成。
当我们需要常见多个子进程时，我们可以考虑使用进程池。如下：
```
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
```
输出结果为：
```
Process(9635) started
Waiting for all sub-processes done ...!
Run tasks as process (9636)
Run tasks as process (9637)
Tasks 9636 runs 0.00 seconds.
Run tasks as process (9638)
Run tasks as process (9639)
Run tasks as process (9636)
Tasks 9638 runs 0.74 seconds.
Tasks 9637 runs 0.84 seconds.
Tasks 9636 runs 2.45 seconds.
Tasks 9639 runs 2.66 seconds.
All tasks completed ...!
```
我们看到四个进程在同时进行。然后依次执行。'apply_async'为非阻塞进程。对应的还有apply函数，其为阻塞进程，其保证一个进程执行完成，才执行下一个进程。
join前必须使用先close()，防止新建子进程。
### subprocess创建进程
我们用subprocess创建进程如下：
```
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
```
输出结果为：
```
Press ENTER or type command to continue
$ nslookup www.python.org
Server:		10.72.17.5
Address:	10.72.17.5#53

Non-authoritative answer:
www.python.org	canonical name = dualstack.python.map.fastly.net.
Name:	dualstack.python.map.fastly.net
Address: 151.101.76.223

Exit code: 0
```
虽然有多种方法创建进程，但是每个方法都有自己的特点和适用情况，请根据需要选择适合自己项目的方法。
### queues实现进程间通信
进程间通常是需要通信的，实现进程间通信有很多种方法。我们实验下，通过queues中实现Process进程间通信。
可实现为：
```
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
```
输出为：
```
Press ENTER or type command to continue
Write Process: 16781 ...
Put A to queue ...
Put B to queue ...
Put C to queue ...
Read Process: 16783 ...
Get A from queue ...
Get B from queue ...
Get C from queue ...
```
