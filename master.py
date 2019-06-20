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
