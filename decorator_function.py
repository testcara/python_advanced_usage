import logging
import time
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger('my-logger')


def decorator(func):
    log.info(func.__name__)

    def wrappper(*args, **kargs):
        log.info(time.time())
        func()
        log.info(time.time())
    return wrappper


@decorator
def func():
    print("I am the main fuction")


func()
