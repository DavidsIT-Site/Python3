# splitting on multiple delimiters
line = 'asdf fjdk; afed, fjek,asdf,        foo'
import re
split = re.split(r'[;,\s]\s*', line)
print(split)



fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

print(''.join(value + delimiter for value, delimiter in zip(values,delimiters)))

fields = re.split(r'(?:,|;|\s)\s*', line)
print(fields)
