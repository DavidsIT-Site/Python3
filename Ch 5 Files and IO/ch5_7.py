# reading and writing compressed datafiles
# gzip or bz2 compression

# write compressed data to file
text = "my block text is not blocky enough"

import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

text = "my block text is not blocky enough2"
import bz2

with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

with gzip.open('somefile.gz', 'rt') as f:
    print(f.read())

with bz2.open('somefile.bz2', 'rt') as f:
    print(f.read())


#compression modules work with various file like objects: sockets, pipes and in memory files

f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()
