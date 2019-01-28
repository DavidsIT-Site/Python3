# flattening a nested sequence

from collections.abc import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3,[4, 2]], 1]
# print(items)
for item in flatten(items):
    print(item)

items = ['Dave', 'Paula', ['Ricky', 'Clay'], 'john']
print(items)
for item in flatten(items):
    print(item)
