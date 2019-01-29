# a function that accepts any number of arguments
def avg(first, *rest):
    return (first+sum(rest)/(1+len(rest)))

print(avg(1,2))
print(avg(1, 2, 5, 6, 7, 8))
print(avg(1, 2, 9, 8, 1, 1))

def make_element(x, *args, **kwargs):
    print("{}".format((args)))
    print("{}".format((kwargs)))
c = make_element(1, 2, 3, size = 'huge')


def make_element2(x, *args, y, **kwargs):
    print("{}".format((args)))
    print("{}".format((kwargs)))
    print("{}".format((x)))
    print("{}".format((y)))
c = make_element2(1, 2, 3, y=2, size = 'huge')
