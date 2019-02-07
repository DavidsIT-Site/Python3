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
        super(SubPerson, SubPerson).name.__set__(self.value)