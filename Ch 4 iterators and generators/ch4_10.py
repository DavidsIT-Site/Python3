# iterating over the index- value pairs of a sequence
# keeping track of a sequence elements in a sequence

list = ['a', 'b', 'c', 'd']
for id, value in enumerate(list):
    print('pos {} holds the value: {}'.format(id, value))

print()
for id, value in enumerate(list, 1):
    print('pos {} holds the value: {}'.format(id, value))


data = [(1, 2), (3, 4), (4, 5), (6, 7), (8, 9)]
for n, (x, y) in enumerate(data):
    print('{}-object; {}:{}'.format(n, x, y))
