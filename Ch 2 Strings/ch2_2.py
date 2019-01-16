# matching text at start or end of a string can be done with str.startswith() or str.endswith()
filename = "spam.txt"
print(filename.endswith('.txt'))
print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))


# multiple choices
import os
filenames = os.listdir('.')
print(filenames)

print([name for name in filenames if name.endswith('py')])


from urllib.request import urlopen


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

print(read_data(url))

choices = ['http', 'https', 'ftp']
print(url.startswith(tuple(choices)))

from fnmatch import fnmatch, fnmatchcase
vars = []
vars.append(fnmatch('foo.txt', '*.txt'))
vars.append(fnmatch('foo.txt', '?oo.txt'))
vars.append(fnmatch('Dat45.csv', 'Dat[0-9]*'))

print(vars)