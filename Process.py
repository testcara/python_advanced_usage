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
