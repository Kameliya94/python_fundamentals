stock = input().split()
bakery = {}

for item in range(0, len(stock), 2):
    food = stock[item]
    quantity = int(stock[item + 1])
    bakery[food] = quantity

print(bakery)