# combine and concat strings
parts = ['hello', 'worlds', 'this', 'is']
print(', '.join(parts))

data = ['ACME', 50, 91.1]
print(', '.join(str(pos) for pos in data))