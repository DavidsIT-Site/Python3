#  You want to strip unwanted characters such as whitespace, from the beginning, middle, or end of a text string

s = '          \t    hello worlds    \n \t'
t = s.strip()
print(s)
print(t)

ls = s.lstrip()
rs = s.rstrip()
print(ls)
print(rs)
