number_of_lines = int(input())
capacity_tank = 255

for line in range(number_of_lines):
    liters_of_water = int(input())

    if capacity_tank >= liters_of_water:
        capacity_tank -= liters_of_water
    else:
        print("Insufficient capacity!")
        continue

print(255 - capacity_tank)