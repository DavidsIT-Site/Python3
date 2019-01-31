# functions with default arguments

def spam(a, b=42):
    print(a, b)

print(spam(1))
print(spam(1, 200))

_no_value = object()


def spam2(a, b=_no_value):
    if b is _no_value:
        print("no value supplied for b")
        b = []
    elif b is None:
        print("None supplied for b")
        b = []
    print(a, b)

print(spam2(1,1))
print(spam2(1, [200, 50]))

