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


def callsimeple_conroutine():
    sc = simple_coroutine()
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
