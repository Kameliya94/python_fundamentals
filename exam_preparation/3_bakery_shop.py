stocked_food = {}
sold_food = 0

while True:
    command = input().split()


    if command[0] == "Complete":
        break

    elif command[0] == "Receive":
        quantity = int(command[1])
        food = command[2]
        if quantity <= 0:
            continue
        if food not in stocked_food:
            stocked_food[food] = quantity
        else:
            stocked_food[food] += quantity

    elif command[0] == "Sell":
        quantity = int(command[1])
        food = command[2]

        if food not in stocked_food:
            print(f"You do not have any {food}.")
        else:
            if stocked_food[food] < quantity:
                sold = stocked_food[food]
                sold_food += sold
                print(f"There aren't enough {food}. You sold the last {sold} of them.")
                del stocked_food[food]
            else:
                stocked_food[food] -= quantity
                sold_food += quantity
                print(f"You sold {quantity} {food}.")
                if stocked_food[food] == 0:
                    del stocked_food[food]

for food, quantity in stocked_food.items():
    print(f"{food}: {quantity}")
print(f"All sold: {sold_food} goods")