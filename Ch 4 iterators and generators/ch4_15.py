# iterating in sorted order over merged sorted iterables
import heapq
a = [1, 2, 4, 7]
b = [2, 3, 6, 9]
for c in heapq.merge(a, b):
    print(c)