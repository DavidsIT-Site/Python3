# creating a new kind of class or instance attribute# creating a new kind of class or instance attribute

class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('expected an int')
        instance.__dict__[self.name] = value


    def __delete__(self, instance):
        del instance.__dict__[self]


class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(12, 3)
my_int = Integer(1)
print('myint:   {}   {}'.format(my_int, my_int.name))
print('{}   {}'.format(p.x, p.y))


my_int2 = Integer('1')
print('myint2:  {}   {}'.format(my_int2, my_int2.name))
# p2 = Point('1', 3)

# https://python-forum.io/Thread-Unexpected-expected-type-error-result