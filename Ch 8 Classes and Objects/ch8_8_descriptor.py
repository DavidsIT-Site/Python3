class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('expected a string')
        instance.__dict__[self.name] = value

class Person:
    name = String('name')
    def __init__(self, name):
        self.name = name

class SubPerson(Person):
    @property
    def name(self):
        print("getting name")
        return super().name

    @name.setter
    def name(self, value):
        print('setting name to {}'.format(value))
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


p = Person("david")
print(p.name)
p = SubPerson("david")
print(p.name)
# by the time you read this, subclassing of setter and deleter
# methods might be somewhat simplified.