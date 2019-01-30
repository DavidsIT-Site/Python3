# capturing values from anonymous functions
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

print(a(10))
print(b(10))


x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y

print(a(10))
print(b(10))

funcs = [lambda z, n=n: z+n for n in range(5)]
for func in funcs:
    print(func(0))