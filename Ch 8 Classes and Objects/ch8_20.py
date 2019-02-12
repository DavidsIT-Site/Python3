# calling a method on an objecctg given the name as an string
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point: ({}, {})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


P = Point(2, 3)
d = getattr(P, 'distance')(0, 0)
print('{}   {}'.format(P, d))



import operator
result = operator.methodcaller('distance', 0, 0)(P)
print(result)

points = [
    Point(1, 9),
    Point(1, 7),
    Point(1, 8),
    Point(5, 9),
    Point(2, 9)
]

print(points)
points.sort(key=operator.methodcaller('distance', 0, 0))
print('\n{}'.format(points))


shorthand_dist = operator.methodcaller('distance', 0, 0)
print(shorthand_dist(P))

