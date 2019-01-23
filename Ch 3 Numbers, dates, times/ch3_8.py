# with fractions
from fractions import Fraction
a = Fraction(3, 4)
print(a)
c = a*a
print("{}   {}    {}  {}".format(c.numerator, c.denominator, c, float(c)))

d = float(c)
print(d)
print(Fraction(*d.as_integer_ratio()))