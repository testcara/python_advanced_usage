## python 协程
### 什么是协程
我们在前几章学过多进程和多线程并发，“协程”又称“微线程”，在一个线程中会有很多函数，我们称这些为子程序，在子程序执行过程中中断去执行别的子程序，而别的子程序在适当的时候也可以中断回来继续执行之前的子程序，这个过程称之为协程。协程可以理解为一种多程序/函数并发。

子程序/函数在所有语言中都是层级调用，比如A调用B，B调用C, C执行完毕返回，B执行完毕返回，A执行完毕返回。但是在协程中，则会出现C未执行完毕，产生中断，而去执行B或者A，执行B或者A后，返回C继续执行。在外面看来，这一个线程出现了函数A，B和C并发的状况，而其如何并发，区别与程序自身我们的定义。
让我们来实践下：
```
import time
import sys 

def simple_coroutine():
  print("---> start ...")
  for i in [1, 2, 3, 4, 5]: 
      x = yield
      print("The current function: %s" % (sys._getframe().f_code.co_name))
      print("---> I am yielding, %s ..." % i)
      time.sleep(1)
      print("---> received ...", x)
  print("[End] The current function: %s" % (sys._getframe().f_code.co_name))                                                                             
def callsimple_coroutine():
  sc = simple_coroutine()
  # 生成器，可以使用send方法执行函数
  sc.send(None)

  for i in [6, 7, 8, 9]: 
      print("The current function: %s" % (sys._getframe().f_code.co_name))
      sc.send(i)
  print("[End] The current function: %s" % (sys._getframe().f_code.co_name))

if __name__ == "__main__":
  print("[Start] The current function: %s" %
        (sys._getframe().f_code.co_name))
  callsimeple_conroutine()
  print("[End] The current function: %s" % (sys._getframe().f_code.co_name))
```
输出为：
```
[Start] The current function: <module>
---> start ...
The current function: callsimple_coroutine
The current function: simple_coroutine
---> I am yielding, 1 ...
---> received ... 6
The current function: callsimple_coroutine
The current function: simple_coroutine
---> I am yielding, 2 ...
---> received ... 7
The current function: callsimple_coroutine
The current function: simple_coroutine
---> I am yielding, 3 ...
---> received ... 8
The current function: callsimple_coroutine
The current function: simple_coroutine
---> I am yielding, 4 ...
---> received ... 9
[End] The current function: callsimple_coroutine
[End] The current function: <module>
```
我们看到main函数调用callsimple_coroutine函数，callsimple_coroutine函数调用simple_coroutine函数。按照函数是层级调用来讲，应该先返回simple_coroutine，然后callsimple_routine,但是实际上这两个程序是在不断的切换。这就是协程，也可以称为不同程序之间在一个线程里协同工作。

### 用协程实现生产者和消费者模型
 我们曾使用多线程和多进程来实现生产者和消费者模型。
 现在我们是使用协程实现该模型
```
def consumer():
  print("---> [Start] Consumer ...")
  result = 0 
  while True:
      data = yield result
      print("---> [Consumer] Consume the producer: %s" % data)
      result = data * data                                                                                      
def producer(c):
  print("---> [Start] Producer ...")
  # active the consumer
  c.send(None)
  for i in [1, 2, 3]: 
      print("---> [Producer] Produce: %s" % i)
      result = c.send(i)
      print("---> [Producer] Got the result from the consumer: %s" % result)

c = consumer()
producer(c)
```
执行结果为：
```
---> [Start] Producer ...
---> [Start] Consumer ...
---> [Producer] Produce: 1
---> [Consumer] Consume the producer: 1
---> [Producer] Got the result from the consumer: 1
---> [Producer] Produce: 2
---> [Consumer] Consume the producer: 2
---> [Producer] Got the result from the consumer: 4
---> [Producer] Produce: 3
---> [Consumer] Consume the producer: 3
---> [Producer] Got the result from the consumer: 9
```
则我们看到一旦生产任务，可以马上切换到消费任务，消费生产目标。
### async/await 实现简单的协程
python不同的版本对协程的支持和实现是不同的。我们这里以3.7版本为例来讲解协程的实现。在python3.7中，协程通过 async/await 语法进行声明，是编写异步应用的推荐方式。
最简单的如下：
```
import asyncio
import time

async def main():
  print("[%s] hello" % (time.ctime()))
  await asyncio.sleep(1)
  print("[%s] world!" % (time.ctime()))
                                                
asyncio.run(main())
```
则输出为：
```
[Sun Jun 23 21:48:03 2019] hello
[Sun Jun 23 21:48:04 2019] world!
```
这里用到的主要关键用法有：
* asyncio.run() 执行协程函数
* await等待协程执行完成。其实，await可以还可以等待任务和Future对象
### async/await实现并行的多协程
如果我们只是用async和awati是可以实现协程的。多协程如下：
```
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print("[%s] %s" % (time.ctime(), what))

async def main():
    print(f"started at {time.strftime('%X')}")
  
await say_after(1, 'hello')
await say_after(4, 'world')                                                                                             
print(f"finished at {time.strftime('%X')}")=
asyncio.run(main())
```
输出为：
```
started at 21:56:59
[Sun Jun 23 21:57:00 2019] hello
[Sun Jun 23 21:57:04 2019] world
finished at 21:57:04
```
我们可以看到，其用了5s。如果我们为上例中的两个协程函数创建task, 则会如下：
```
import asyncio
import time

async def say_after(delay, what):
await asyncio.sleep(delay)
print("%s %s" % (time.ctime(), what))
                                    
async def main():
task1 = asyncio.create_task(say_after(1, "Hello"))
task2 = asyncio.create_task(say_after(4, " world!"))

# wait until the tasks are completed
await task1
await task2

print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```
输出为：
```
started at 22:16:27
Sun Jun 23 22:16:28 2019 Hello
Sun Jun 23 22:16:31 2019  world!
finished at 22:16:31
```
则时间为4s，则少了1s，是因为task并发执行。

### 协程中一些重要的知识点：
我们来梳理以下协程中一些重要的知识点，这些知识点包括我们以上提到内容，以及一些新的内容。
* 实现协程的不仅仅是asyncio，tornado和gevent都实现了类似的功能。
* coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象可以由函数直接调用执行，协程对象可以通过函数直接调用执行，可以为其创建task并发执行，可以注册到事件循环中，由事件循环调用。
* task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。
* async/await：用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。

协程中还有许多用法，我们将将一些关键链接放在这里：
* https://docs.python.org/zh-cn/3.7/library/asyncio-task.html#shielding-from-cancellation

* https://www.ibm.com/developerworks/cn/analytics/library/ba-on-demand-data-python-3/index.html
