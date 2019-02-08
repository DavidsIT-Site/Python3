# extending a propoerty in a subclass

class Person:
    def __init__(self, name):
        self.name = name


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError('can\'t delete attribute')

a1 = Person("david")
print(a1.name)


class SubPerson(Person):
    @property
    def name(self):
        print('getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('setting name to ', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting self')
        super(SubPerson, SubPerson).name.__delete__(self)

s = SubPerson("John Doe")
print(s)
print(s.name)
s.name = "David"
#s.name = 12

class SubPerson2(Person):

    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

s2 = SubPerson2("john doe")
print(s2)
print(s2.name)
s2.name = "test"
print(s2.name)
