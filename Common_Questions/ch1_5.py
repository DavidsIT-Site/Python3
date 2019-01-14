"""
Implementing a priority queue
"""
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "Item({!r})".format(self.name)

q = PriorityQueue()
i1 = Item('foo')
i2 = Item('foo2')
q.push(i1, 99)
q.push(i2, 5)
q.push(Item('one'), 1)
q.push(Item('one-hundred'), 100)


print(q.pop())

print(q.pop())
print(q.pop())
print(q.pop())

#1.6 mapping keys
d ={
    'a': [1,2,3],
    'b': [6,4]
}

e = {
    'a': {1, 2, 3},
    'b': {4,6}
}
print(d)

from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(5)
print(d)
d = defaultdict(set)
d['a'].add(2)
print(d)

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(2)

print(d)

#discussion about multivalued dictionary
pairs = ([('foo', 1), ('bar', 2)])
d = {}
for key, value, in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

#pythonic
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)

from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
for key in d:
    print(key, d[key])
import json
print(json.dumps(d))


