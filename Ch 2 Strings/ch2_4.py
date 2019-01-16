# matching and searching text patterns
text = "yeah, but no, but yeah, but no, but yeah"

text1 = "11/27/2017"
text2 = "Nov 27, 2012"

import re
if re.match(r'\d+/\d+', text1):
    print('yes')
else:
    print('no')


if re.match(r'\d+/\d+/\d+', text2):
    print("yes")
else:
    print("no")

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('np')

text = "Today is 11/27/2012. PyCon starts 3/13/2013"
print(datepat.findall(text))




datepat = re.compile(r'((\d+)/(\d+))/(\d+)')

m = datepat.match('11/27/2012')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group(4))
text = "Today is 11/27/2012. PyCon starts 3/13/2013"
for m in datepat.finditer(text):
    print(m.groups())
