stock = {}

while True:
    command = input().split(": ")

    if command[0] == "statistics":
        break

    product = command[0]
    quantity = int(command[1])

    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

print(f"Products in stock:")
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")