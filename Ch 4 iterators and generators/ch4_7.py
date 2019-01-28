# you want sliced data from an iterator but normal slicing [y:z] doesn't work
def count(n):
    while True:
        yield n
        n += 1

c = count(0)
#c[10:20]
import itertools
for x in itertools.islice(c,10,20):
    print(x)

    # islice consumes data. can't undo iterators. maybe a list instead
