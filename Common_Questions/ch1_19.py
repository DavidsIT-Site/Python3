# transformations and reductions
nums = [1, 2, 3, 4, 5, 6, 7]
s = sum(x * x for x in nums)
print(s)


# do any python files exist
import os
files = os.listdir("folder")
if any(name.endswith('.py') for name in files):
    print('There be Python!')
else:
    print('No pythons found')

# output tuple as csv
structure = ('ACME', 50, 123.45)
print(','.join(str(x) for x in structure))


# data reduction
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65},
    {'name': 'FB', 'shares': 19}
]
min_shares = min(data['shares'] for data in portfolio)
Min_shares = min(portfolio, key=lambda data: data['shares'])
print(min_shares)
print(Min_shares)

sum_gen = (x * x for x in nums)
s = sum(sum_gen)
S = sum(x * x for x in nums)
print(s)
print(S)

