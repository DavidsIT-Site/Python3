# defining more than one constructor in a class

import time

class Date:
    def __init__(self, *args):
        if len(args) == 0:
            t = time.localtime()
            args = (t.tm_year, t.tm_mon, t.tm_mday)
        self.year, self.month, self.day = args

a = Date(2012, 2, 11)

print(a.year)

b = Date()
print(b.year)

# better clarity with
# date.today()