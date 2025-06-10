count_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_price = 0

for lost_fights in range(1, count_of_lost_fights + 1):
    if lost_fights % 2 == 0:
        total_price += helmet_price
    if lost_fights % 3 == 0:
        total_price += sword_price
    if lost_fights % 2 == 0 and lost_fights % 3 == 0:
        total_price += shield_price
    if lost_fights % 12 == 0:
        total_price += armor_price

print(f"Gladiator expenses: {total_price:.2f} aureus")