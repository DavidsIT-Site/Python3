# changing the string representation of instances
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'REPR Pair ({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return 'STR Pair ({0.x!s}, {0.y!s})'.format(self)

p = Pair(5, 6)

print(p)
print(repr(p))
