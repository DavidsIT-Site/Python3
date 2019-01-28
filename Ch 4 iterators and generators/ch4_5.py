# iterating in reverse

a = [1, 2, 3, 4, 5]
for x in reversed(a):
    print(x)

f = open('passwd')
for line in reversed(list(f)):
    print(line)



class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


count = Countdown(5)
for line in reversed(count):
    print(line)
count = Countdown(5)
##next(count)
iterable = iter(count)
print(next(iterable))