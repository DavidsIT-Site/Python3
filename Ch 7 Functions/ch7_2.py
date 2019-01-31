# functions that only accept keyword arguments

def mininum(*values, filter=None):
    m = min(values)
    if filter is not None:
        m = filter if filter > m else m
    return m

print(mininum(1, 2, 3, 4,5))
print(mininum(1, 2, 3, 4, 5, filter=2))
print(help(mininum))


# functions that only accept keyword arguments

def maximum(*values, filter=None):
    m = max(values)
    if filter is not None:
        m = filter if filter < m else m
    return m

print(maximum(1, 2, 3, 4,5))
print(maximum(1, 2, 3, 4, 5, filter=2))
print(help(maximum))
