# named sequences

from collections import namedtuple
Subscriber = namedtuple('Subcriber', ['addr','joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(Subscriber)
print(sub)
print(sub.addr)
print(sub.joined)

print("Length: {}".format(len(sub)))


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total
s = Stock('ACME', shares = 100, price = 123.45)
print(s)

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)

def dict_to_stock(dict):
    return stock_prototype._replace(**dict)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
A = dict_to_stock(a)
print(A)

b = {'name':'ACME', 'shares': 100, 'price':123.45, 'date': '12/17/2012'}
B = dict_to_stock(b)
print(B)
B = Stock(name='ACME', shares=100, price=123.45, date='12/17/2012', time=None)
print(B)


