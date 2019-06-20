## python 分布式多进程
我们在前两章节中演示了如何在一个进程中创建子进程实现多进程，并通过queue进行
通信。如果创建独立的多进程，并保持多进程之间的通信，当多进程在同一个服务器端
一起工作让系统负重不堪时，如何处理，就是本章要讨论和解决的问题。

multiprocessing模块中的managers子模块将多进程分布到多个机器上。一个服务
进程作为调度者，放在master端，通过网络发布任务，worker端通过网络获取任务，
执行任务，并将结果返回给master端。这样就将压力分布在不同的机器上，实现了多进程
的分布式。


具体实现如下：
master.py
```
from multiprocessing import Queue
from multiprocessing.managers import BaseManager
import time

# create tasks queues
task_queue = Queue()
# create results queues
result_queue = Queue()

def get_task():
    return task_queue

def get_result():
    return result_queue

class TaskManagers(BaseManager):
    # do nothing
    pass

# register queue to networks
# register(registered queue, real queue)
TaskManagers.register('get_task_queue', callable=get_task)
TaskManagers.register('get_result_queue', callable=get_result)

# binding to network address, port and authkey
mgr = TaskManagers(address=('127.0.0.1', 4444), authkey=b'python3')
# start the manager
mgr.start()

# get the queues fromn network
task = mgr.get_task_queue()
result = mgr.get_result_queue()

data_list = [1, 2, 3, 4, 5, 6]

# publish tasks
for data in data_list:
    task.put(data)
    print("[Master] - %s - put data into tasks: %s" % (time.ctime(), data))

# get results:
while True:
    if result.empty():
        print(
            "[Master] - %s - No results has been returned!, Wait for 5s..." %
            (time.ctime()))
        time.sleep(5)
    else:
        data = result.get(timeout=10)
        print("[Master] - %s - get result from queues: %s" %
              (time. ctime(), data))


```
worker.py
```
from multiprocessing.managers import BaseManager
import time


class TaskManager(BaseManager):
    pass

def do_tasks(n):
    if (n % 2 == 0):
        return 'passed'
    else:
        return 'faild'

# binding to network address
msg = TaskManager(address=('127.0.0.1', 4444), authkey=b'python3')
# register the queues
msg.register('get_task_queue')
msg.register('get_result_queue')
# establish the connection
msg.connect()

# get the registered network queue
task = msg.get_task_queue()
result = msg.get_result_queue()

# get tasks, do tasks then return results
while True:
    if not (task.empty()):
        data = task.get(timeout=5)
        print("[Worker] - %s - doing tasks with parameter %s" % (time.ctime(),
                                                                 data))
        time.sleep(1)
        final_result = do_tasks(data)
        print("[Worker] - %s - Return result: %s" %
              (time.ctime(), final_result))
        result.put(final_result)
    else:
        print("[Worker] - %s - Have completed tasks! Wait for 5s" %
              (time.ctime()))
        time.sleep(5)
```
让我们启动master和worker,然后其输出为：
master的输出为：
```
[wlin@wlin python_advanced_usage]$ python3 master.py 
[Master] - Thu Jun 20 14:42:05 2019 - put data into tasks: 1
[Master] - Thu Jun 20 14:42:05 2019 - put data into tasks: 2
[Master] - Thu Jun 20 14:42:05 2019 - put data into tasks: 3
[Master] - Thu Jun 20 14:42:05 2019 - put data into tasks: 4
[Master] - Thu Jun 20 14:42:05 2019 - put data into tasks: 5
[Master] - Thu Jun 20 14:42:05 2019 - put data into tasks: 6
[Master] - Thu Jun 20 14:42:05 2019 - No results has been returned!, Wait for 5s...
[Master] - Thu Jun 20 14:42:10 2019 - No results has been returned!, Wait for 5s...
[Master] - Thu Jun 20 14:42:15 2019 - No results has been returned!, Wait for 5s...
[Master] - Thu Jun 20 14:42:20 2019 - get result from queues: faild
[Master] - Thu Jun 20 14:42:20 2019 - get result from queues: passed
[Master] - Thu Jun 20 14:42:20 2019 - get result from queues: faild
[Master] - Thu Jun 20 14:42:20 2019 - No results has been returned!, Wait for 5s...
[Master] - Thu Jun 20 14:42:25 2019 - get result from queues: passed
[Master] - Thu Jun 20 14:42:25 2019 - get result from queues: faild
[Master] - Thu Jun 20 14:42:25 2019 - get result from queues: passed
[Master] - Thu Jun 20 14:42:25 2019 - No results has been returned!, Wait for 5s...
[Master] - Thu Jun 20 14:42:30 2019 - No results has been returned!, Wait for 5s...
[Master] - Thu Jun 20 14:42:35 2019 - No results has been returned!, Wait for 5s...

```
worker的输出为：
```
[wlin@wlin python_advanced_usage]$ python3 worker.py 
[wlin@wlin python_advanced_usage]$ python3 worker.py 
[Worker] - Thu Jun 20 14:42:17 2019 - doing tasks with parameter 1
[Worker] - Thu Jun 20 14:42:18 2019 - Return result: faild
[Worker] - Thu Jun 20 14:42:18 2019 - doing tasks with parameter 2
[Worker] - Thu Jun 20 14:42:19 2019 - Return result: passed
[Worker] - Thu Jun 20 14:42:19 2019 - doing tasks with parameter 3
[Worker] - Thu Jun 20 14:42:20 2019 - Return result: faild
[Worker] - Thu Jun 20 14:42:20 2019 - doing tasks with parameter 4
[Worker] - Thu Jun 20 14:42:21 2019 - Return result: passed
[Worker] - Thu Jun 20 14:42:21 2019 - doing tasks with parameter 5
[Worker] - Thu Jun 20 14:42:22 2019 - Return result: faild
[Worker] - Thu Jun 20 14:42:22 2019 - doing tasks with parameter 6
[Worker] - Thu Jun 20 14:42:23 2019 - Return result: passed
[Worker] - Thu Jun 20 14:42:23 2019 - Have completed tasks! Wait for 5s
[Worker] - Thu Jun 20 14:42:28 2019 - Have completed tasks! Wait for 5s
[Worker] - Thu Jun 20 14:42:33 2019 - Have completed tasks! Wait for 5s
```
在我们的实验中，我们采用了轮询的机制去获取任务和处理任务并返回结果。
