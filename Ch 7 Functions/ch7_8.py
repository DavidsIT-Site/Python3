# making n- argument callable work with fewer arguments
from functools import partial

def spam(a, b, c, d):
    print(a, b, c, d)


print(spam(1, 2, 3, 4))

spam1 = partial(spam, 1)
print(spam1(2,3,4))

spam2 = partial(spam, 1, 2, d=42)
print(spam2(4))


points = [(1, 2), (4, 5), (7, 8), (8, 9)]

import math
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2-x1, y2-y1)

pt = points[1]
print(pt)
points.sort(key=partial(distance, pt))
print(points)