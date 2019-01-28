# printing with a different separator or line ending
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=', ')
print('ACME', 50, 91.5, sep=', ', end="!!\n")

row = ('ACME', 50, 91.5)
print(*row, sep=',')
