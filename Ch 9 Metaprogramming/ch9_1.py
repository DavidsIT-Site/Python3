# putting a wrapper around a function

import time
from functools import wraps

def timethis(func):
    """Decorator that reports the execution time"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@timethis
def countdown(n):
    """ counts down"""
    while n > 0:
        n -= 1


countdown(10000)
countdown(10000000)