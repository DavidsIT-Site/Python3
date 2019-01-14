# Calculating with dictionaries

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.65
}

print(prices)

min_price = min(zip(prices.values(), prices.keys()))
print("MIN: {}".format(min_price))

max_price = max(zip(prices.values(), prices.keys()))
print("MAX: {}".format(max_price))

print(min(prices))
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

min_value = prices[min(prices, key=lambda k: prices[k])]
min_name = min(prices, key=lambda k: prices[k])
print(min_value)
print(min_name)
