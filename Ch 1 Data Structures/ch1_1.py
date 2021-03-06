"""
Data scientists are precise
any sequence or iterable can be unpacked using an assignment operation
This means that one group of variable names is a group of values.
"""
p = (4, 5)
x, y = p
print("x is: %d" % x)
print("y is: %d" % y)

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print("%s: $%d purchased %s" % (name, price*shares, date))
name, shares, price, (year, month, day) = data
print("%s: $%d purchased %s" % (name, price*shares, day))

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

record = ('David', 'David@DavidsIT.Site', '706-452-3484', 'nan')
name, email, *phone_numbers = record
print(phone_numbers)


def trail_avg(sales_record):
    *trailing_qtrs, current_qts = sales_record
    trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    return trailing_avg - current_qts


records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x,y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print("name: %s\nhomedir: %s" % (uname, homedir))
print("fields: %s\nsh: %s"% (fields, sh))

items = [1, 10, 7, 5, 0, 9]

head, *tail = items
print("head: %s \ttail: %s" % (head, tail))

def recus_sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
print(recus_sum(items))

from collections import deque
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)

q = deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.appendleft(6)
print(q)
q.pop()
print(q)
q.popleft()
print(q)

#page 7
#1.4 List of the lasrgest or smallest items in a collection
import heapq
nums = [1, 2, 5, 6, 23, -4, 54, 2, 0]
print(heapq.nsmallest(3, nums))
print(heapq.nlargest(3, nums))

#how to take a heap of data stuctures
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'nane': 'APPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21},
    {'name': 'HPQ', 'shares': 50, 'price': 32},
    {'name': 'YHOO', 'shares': 23, 'price': 17}
]
inexpensive = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(inexpensive)
print(expensive)

#heap works by converting data into a list  as an ordered heap

print(nums)
heap = list(nums)
heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
print(heap)
