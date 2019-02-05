# creating managed attributes
# type checking / validation

class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def get_first_name(self):
        return self._first_name()

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    def del_first_name(self):
        raise AttributeError('can\'t delete attribute')

    name = property(get_first_name, set_first_name, del_first_name)
I_Am = Person("David")
print(Person)
print(Person.get_first_name)
print(I_Am.set_first_name('me'))
print(I_Am._first_name)
#print(Person.get_first_name(I_Am))

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius ** 2
    @property
    def perimeter(self):
        return 2* math.pi * self.radius

c = Circle(5)
print(c.radius)
print(c.perimeter)