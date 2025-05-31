quantity_of_decoration = int(input())
days_till_christmas = int(input())

christmas_spirit = 0
spend_money = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

for days in range(1, days_till_christmas + 1):

    if days % 11 == 0:
        quantity_of_decoration += 2

    if days % 2 == 0:
        spend_money += ornament_set_price * quantity_of_decoration
        christmas_spirit += 5

    if days % 3 == 0:
        spend_money += (tree_skirt_price + tree_garland_price) * quantity_of_decoration
        christmas_spirit += 13

    if days % 5 == 0:
        spend_money += tree_lights_price * quantity_of_decoration
        christmas_spirit += 17

    if days % 3 == 0 and days % 5 == 0:
        christmas_spirit += 30

    if days % 10 == 0:
        spend_money += tree_skirt_price + tree_garland_price + tree_lights_price
        christmas_spirit -= 20

if days_till_christmas % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {spend_money}")
print(f"Total spirit: {christmas_spirit}")

