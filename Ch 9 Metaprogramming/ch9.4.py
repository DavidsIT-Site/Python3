# defining a decorator that takes arguments
from functools import wraps
import logging

def logged(level, name=None, message=None):
    """
    Add logging to a function. Level of
    logging is the level name, name is the
    logger name, and message - the message log

    """

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print("example  log function")

