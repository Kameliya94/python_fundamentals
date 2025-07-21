events = input().split("|")

energy = 100
coins = 100
bakery_is_open = True

for event in events:
    current_event, value = event.split("-")

    if current_event == "rest":
        initial_energy = energy
        energy += int(value)
        if energy > 100:
            energy = 100
        gained_energy = energy - initial_energy
        print(f"You gained {gained_energy} energy."
              f"\nCurrent energy: {energy}.")

    elif current_event == "order":

        if energy >= 30:
            coins += int(value)
            print(f"You earned {value} coins.")
            energy -= 30
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= int(value):
            coins -= int(value)
            print(f"You bought {current_event}.")
        else:
            print(f"Closed! Cannot afford {current_event}.")
            bakery_is_open = False
            break

if bakery_is_open:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")