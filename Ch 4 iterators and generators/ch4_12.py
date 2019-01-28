# iterating on items in separate containers

from itertools import chain
a = [1, 2, 3, 4]
b = ['z', 'a', 'b']
for x in chain(a, b):
    print(x)

