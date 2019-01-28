# reading and writing binary data

with open('somefile.bin', 'wb') as f:
    f.write(b'Hello Worlds')

#must be bytes and not some other form of data

with open('somefile.bin', 'rb') as f:
    data = f.read()





# file encodings
with open('somefile.bin', 'wb') as f:
     text = 'Hello Worlds'
     f.write(text.encode('utf-8'))

# must be bytes and not some other form of data

with open('somefile.bin', 'rb') as f:
    data = f.read()
    text = data.decode('utf-8')

print(text)