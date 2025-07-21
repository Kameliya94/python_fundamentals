import re

total_cost = 0
list_of_furniture = []
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"


while (command := input()) != "Purchase":
    matches = re.search(pattern, command)
    if matches:
        current_furniture = matches.group(1)
        cost = float(matches.group(2))
        quantity = int(matches.group(3))
        total_cost += cost * quantity
        list_of_furniture.append(current_furniture)

print(f"Bought furniture:")
for furniture in list_of_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")