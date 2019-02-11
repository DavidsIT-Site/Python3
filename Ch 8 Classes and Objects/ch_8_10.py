# using lazily computed properties


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('computing area')
        return math.pi * self.radius **2

    @lazyproperty
    def perimeter(self):
        print('computing perimeter')
        return 2 * math.pi ** self.radius

c = Circle(3.0)
print(c.area)
print(c.perimeter)
print(c.area)
print(c.perimeter)