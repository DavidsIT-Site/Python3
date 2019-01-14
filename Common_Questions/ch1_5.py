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