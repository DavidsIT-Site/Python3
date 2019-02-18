from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator 2')
        return func(*args, **kwargs)
    return wrapper


@decorator2
@decorator1
def add(x, y):
    return x + y


ans1 = add(1, 2)
print(ans1)

ans2 = add.__wrapped__(1, 2)
print(ans2)