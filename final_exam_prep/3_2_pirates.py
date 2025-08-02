targets = {}

while (command := input()) != "Sail":
    city, population, gold = command.split("||")
    if city not in targets.keys():
        targets[city] = {"population": int(population), "gold": int(gold)}
    else:
        targets[city]["population"] += int(population)
        targets[city]["gold"] += int(gold)

while True:
    event = input().split("=>")

    if event[0] == "End":
        break

    if event[0] == "Plunder":
        town = event[1]
        people = int(event[2])
        gold = int(event[3])
        targets[town]["population"] -= people
        targets[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if targets[town]["population"] <= 0 or targets[town]["gold"] <= 0:
            del targets[town]
            print(f"{town} has been wiped off the map!")

    elif event[0] == "Prosper":
        town = event[1]
        gold = int(event[2])

        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        else:
            targets[town]["gold"] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {targets[town]["gold"]} gold.')

if targets:
    print(f'Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:')

    for town, data in targets.items():
        print(f'{town} -> Population: {data["population"]} citizens, Gold: {data["gold"]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")