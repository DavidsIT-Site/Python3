# reading and writing text data

#read entire file as a single string
with open('somefile.txt', 'rt') as f:
    data = f.read()

print(data, end='')
print()
#read entire file as individual lines
with open('somefile.txt', 'rt') as f:
    for line in f:
        print(line, end='')



# write chunks of data
with open('somefile.txt', 'wt') as f:
    f.write("Hello IO\n")
    f.write(data)

with open('somefile2.txt', 'wt') as f:
    print("I am a file", file=f)