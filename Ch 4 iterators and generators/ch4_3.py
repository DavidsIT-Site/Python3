#  new iteration patterns with generators
#  to implement a custom iteration pattern

# generator produces a range of floating-point numbers
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0, 5, .5):
    print(n)

my_list = list(frange(0, 1, .0125))
print(my_list)



def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print("Done counting")

c = countdown(2)
print(c)
print(next(c))
print(next(c))
print(next(c))