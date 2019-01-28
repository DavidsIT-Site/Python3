# iterating over multiple sequences simultaneously

xpoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
ypoints = ['a', 'b', 'c', 'd', 'e', 'f']
zpoints = [101, 78, 37, 15, 62, 55]

for x, y, z in zip(xpoints, ypoints, zpoints):
    print('Experiment{}: {}->{}'.format(x, y, z))

from itertools import zip_longest
for i in zip_longest(xpoints, ypoints, zpoints):
    print(i)

for x, y, z in zip_longest(xpoints, ypoints, zpoints):
    print('Experiment{}: {}->{}'.format(x, y, z))

for x, y, z in zip_longest(xpoints, ypoints, zpoints, fillvalue=0):
    print('Experiment{}: {}->{}'.format(x, y, z))

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 499.1]

s = dict(zip(headers, values))
print(s)
