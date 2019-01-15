# dictionary subsets
prices = {
    'ACME': 45.23,
    'APPL': 612.55,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p1 = {key: value for key, value in prices.items() if value > 200}

tech_names = {'FB', 'HPQ'}
p2 = {key:value for key, value in prices.items() if key in tech_names}
print(p1)
print(p2)



tech_names = {'FB', 'HPQ'}

p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)
p2 = dict((key, value) for key, value in prices.items() if key in tech_names)
print(p2)
