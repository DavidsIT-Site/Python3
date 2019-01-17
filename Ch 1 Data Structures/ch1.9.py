a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
 'w': 10,
 'x': 11,
 'y': 2
}
print(a.keys() & b.keys()) #
print(a.keys() - b.keys())
print(a.items() & b.items())
print(a.items() - b.items())

# page 16

# remove doplicates
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 4, 5, 1, 7, 7, 3, 20]
unique_a = list(dedupe(a))
print("a: {}".format(a))
print("unique_a: {}".format(unique_a))



def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

# what about with a data structure?
a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 2}, {'x': 1, 'y': 3}]
unique_a = list(dedupe(a, key=lambda d: (d['x'])))
print("a: {}".format(a))
print("unique_a: {}".format(unique_a))

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 2}, {'x': 1, 'y': 3}]
unique_a = list(dedupe(a, key=lambda d: (d['x'],d['y'])))
print("a: {}".format(a))
print("unique_a: {}".format(unique_a))

# Without ordering you can do this by making a set
a = [1, 4, 5, 1, 7, 7, 3, 20]

print(a)
unique_a = set(a)
print(unique_a)