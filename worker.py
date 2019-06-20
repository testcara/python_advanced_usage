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
