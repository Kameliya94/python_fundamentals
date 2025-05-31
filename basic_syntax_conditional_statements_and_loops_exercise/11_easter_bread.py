budget = float(input())
price_for_kg_flour = float(input())
price_for_eggs = price_for_kg_flour * 0.75
price_for_l_milk = price_for_kg_flour + (price_for_kg_flour * 0.25)
price_for_loaves_of_bread = price_for_kg_flour + price_for_eggs + (price_for_l_milk / 4)
loaves_of_bread = 0
colored_eggs = 0

while budget >= price_for_loaves_of_bread:

    loaves_of_bread += 1
    colored_eggs += 3
    budget -= price_for_loaves_of_bread

    if loaves_of_bread % 3 == 0:
        colored_eggs = colored_eggs - (loaves_of_bread - 2)

print(f"You made {loaves_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")