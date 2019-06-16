import os


def test_fork():
    print("Prosess {} started...".format(os.getpid()))
    pid = os.fork()
    print(pid)
    if pid == 0:
        print("I am the child prosess({}) and my parent is {}".format(
            os.getpid(), os.getppid()))
    else:
        print("I({}) just created the child prosess({})".format(os.getpid(),
                                                                pid))


test_fork()
