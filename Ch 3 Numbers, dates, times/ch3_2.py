# decimal calculations
a = 2.1
b = 4.2
print(a+b)

from decimal import Decimal
a = Decimal('3.1')
b = Decimal('4.2')
print(a+b)

from decimal import localcontext
a = 3.1
b = 4.2
print(a/b)
a = Decimal('3.1')
b = Decimal('4.2')
print(a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)


with localcontext() as ctx:
    ctx.prec = 53
    print(a/b)
