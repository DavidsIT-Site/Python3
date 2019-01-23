# with infinity and nans

a = float('inf')
b = float('-inf')
c = float('nan')

import math
print("{} {} {}".format(math.isinf(a), math.isinf(b), math.isnan(c)))
print("{} {} {} {}".format(a/a, b+a, c+23, c==c))