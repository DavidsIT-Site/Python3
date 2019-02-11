# simplifying the initialization of data structures
import math

class Structure:
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError ('Expected {} \n Got  {}'.format(self._fields, args))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)


#if __name__ == '__Main__':
class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']

class Circle(Structure):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        print('computing area')
        return math.pi * self.radius **2


    def perimeter(self):
        print('computing perimeter')
        return 2 * math.pi ** self.radius


s = Stock('ACME', 50, 99.9)
p = Point(2, 3)
c = Circle(2)
print(c.perimeter())

# two options in book for *kwargs
# local frame hacking looks to be good for memory optimization
