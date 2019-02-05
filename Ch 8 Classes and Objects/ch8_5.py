# encapsulating names in a class

class A:
    def __init__(self):
        self._internal = 0
        self.public = 1
    def public_method(self):
        print("this is a public method")
    def _internal_method(self):
        print("this is an internal method")

# fight inheritance with __ name on definition
class B:
    def __init__(self):
        self.__private = 0
    def __private_method(self):
        print('this is a private method')
    def public_method(self):
        self.__private_method()
# renamed to _B__private and _B__private_method


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1

    def __private_method(self):
        print('this is a private method')

#__private and __private_method get renamed to _C__private and _C__private_method