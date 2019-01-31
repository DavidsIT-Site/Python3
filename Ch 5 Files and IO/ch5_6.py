# performing i/o operations on a string
# create file like objects that operate on string data
import io

s = io.StringIO()
s.write('hello world\n')
print("this is a test", file=s)
print(s.getvalue())


#use bytesIO instead of string for binary data


