# large numerical arrays
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

print("{}   {}".format(x*2, x+y))  # x+10 does not work like this


import numpy as np
ax = np.array(x)
ay = np.array(y)
print('{}   {}'.format(ax, ay))
print('{}   {}  {}'.format(ax*2, ay+ax, ax+10))

def f(x):
    return 3*x**2 - 2*x + 7
print('{}'.format(f(ax)))

ax_sqrt = np.sqrt(ax)
ax_sin = np.sin(ax)
ax_cos = np.cos(ax)

print('{}\n{}\n{}'.format(ax_sqrt, ax_sin, ax_cos))

grid = np.zeros(shape=(10_000, 10_000), dtype=float)
print(grid)
grid += 10
print(grid)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('a: {}\na[1] row1 {}'.format(a, a[1]))
print('col1: {}'.format(a[:,1]))

print("working with a subregion of an array")
print(a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a)
print(a + [100, 1000, 10000, 10000])


#  numpy conditionals
out = np.where(a<10, a, 10)
print(out)