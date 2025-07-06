stock = input().split()
requested = input().split()
products = {}

for item in range(0, len(stock), 2):
    food = stock[item]
    quantity = int(stock[item + 1])
    products[food] = quantity

for item in requested:
    if item in products:
        print(f"We have {products[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")