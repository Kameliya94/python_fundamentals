cells = input().split("#")
amount_of_water = int(input())
effort = 0
total_fire = 0
put_out_cells = []

for cell in cells:
    type_of_fire, value = cell.split(" = ")
    value = int(value)

    if type_of_fire == "High" and 81 <= value <= 125:
        if amount_of_water >= value:
            amount_of_water -= value
            effort += value * 0.25
            put_out_cells.append(value)
            total_fire += value
        else:
            continue
    elif type_of_fire == "Medium" and 51 <= value <= 80:
        if amount_of_water >= value:
            amount_of_water -= value
            effort += value * 0.25
            put_out_cells.append(value)
            total_fire += value
        else:
            continue
    elif type_of_fire == "Low" and 1 <= value <= 50:
        if amount_of_water >= value:
            amount_of_water -= value
            effort += value * 0.25
            put_out_cells.append(value)
            total_fire += value
        else:
            continue

print("Cells:")
for cell in put_out_cells:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")