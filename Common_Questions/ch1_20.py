# combining multiple mappings into single mapping
a = {'x': 'David', 'y': 0, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap
a_b = ChainMap(a,b)
print(a_b['x'])
print(len(a_b))
print(a_b.keys())
print(a_b.values())
print(a_b.keys())
print(a_b.values())

print(a_b['z'])
a_b['z'] = 5
print(a_b['z'])
print(a_b.values())
del a_b['y']
print(a_b.values())


values = ChainMap()
values['x'] = 1
print(values)
values = values.new_child()
values['y'] = 2
values['x'] = 2
print(values)
values = values.new_child()
values['y'] = 3
values['x'] = 3
print(values)

merged = dict(a)
merged.update(b)
print(merged)


a = {'x': 'David', 'y': 0, 'z': 3}
b = {'y': 2, 'z': 4}

merge = dict(b)
print(merge)
merge.update(a)
print(merge)
a['x'] = "john"
print("merge: {} ".format(merge))
merge.update(a)
print("merge: {} ".format(merge))

a = {'x': 'David', 'y': 0, 'z': 3}
b = {'y': 2, 'z': 4}

merge = ChainMap(a, b)
print(merge)
a['x'] = "john"
print(merge)
