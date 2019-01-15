# filtering sequence

mylist = [1, 4, -5, 10, -7, 2, 3, -1, 0]
pos_filter = [n for n in mylist if n > 0]
print(pos_filter)
neg_filter = [n for n in mylist if n < 0]
print(neg_filter)



mylist = [1, 4, -5, 10, -7, 2, 3, -1, 0]
pos_gen_filter = (n for n in mylist if n > 0)
for x in pos_gen_filter:
    print(x)

values = ['1', '2', '-3', '-', '4', 'n/a', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int,values))
print(ivals)


mylist = [1, 3, 4, -5, 10, -7, 2, 4, -1]
import math
print([math.sqrt(n) for n in mylist if n > 0])

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 E 8TH',
    '5645 N RAVESWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE'
]
print(addresses)

counts = [0, 3, 10, 4, 1, 7, 6]
from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(addresses,more5)))
