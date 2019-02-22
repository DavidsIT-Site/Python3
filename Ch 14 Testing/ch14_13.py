# profiling and timing your program
from timeit import timeit
print(timeit('math.sqrt(2)', 'import math', number=10000000))
print(timeit('sqrt(2)', 'from math import sqrt', number=10000000))