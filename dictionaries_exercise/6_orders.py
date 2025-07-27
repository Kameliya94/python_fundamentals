items = {}

while (command := input()) != "buy":
    item, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if item not in items.keys():
        items[item] = [price, quantity]
    else:
        items[item][0] = price
        items[item][1] += quantity

for item, (price, quantity) in items.items():
    total = price * quantity
    print(f"{item} -> {total:.2f}")