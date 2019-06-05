import logging
import time
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger('my-logger')


def decorator(func):
    log.info(func.__name__)

    def wrappper(one_instance):
        log.info(time.time())
        func(one_instance)
        log.info(time.time())
    return wrappper


class Method(object):
    @decorator
    def func(self):
        print("I am the main fuction")


p1 = Method()
p1.func()
