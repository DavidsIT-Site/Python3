
ssd = "QuickDrive1024-0818"
drive_info = ssd[10:14]
print(drive_info)
items = [0, 1, 2, 3, 4, 5, 6, 7]
a = slice(2, 4, 1)
print(items)
print(items[a])

items[a] = [111, 999]
print(items)
del items[a]
print(items)
