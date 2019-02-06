# creating managed attributes

class Person:
    def __init__(self, fist_name):
        self.first_name = fist_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError('can\'t delete attribute')

a = Person("David")
print(a.first_name)
b = Person("42")
print(b.first_name)

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    #@property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(3.1)
print(c)
print(c.area)
print(c.perimeter())

