# preserving function metadata when writing decorators
# by default decorators when applied cause important metadata
# such as the name, doc string, annotations, and calling signature are lost


import time
from functools import wraps
from inspect import signature

def timethis(func):
    """Decorator that reports the execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@timethis
def countdown(number:int):
    """ counts down"""
    while number > 0:
        number -= 1

print('{} {} {}'.format(countdown.__name__, countdown.__doc__, countdown. __annotations__))
countdown(10000)
countdown(10000000)

print(signature(countdown))