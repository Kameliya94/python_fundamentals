plants_rarity = {}
n = int(input())

for _ in range(n):
    plant, rarity = input().split("<->")
    plants_rarity[plant] = {"rarity": int(rarity), "ratings": []}

while (command := input()) != "Exhibition":
    current_command, second_command_for_split = command.split(": ")

    if current_command == "Rate":
        plant, rating = second_command_for_split.split(" - ")
        if plant not in plants_rarity.keys():
            print("error")
            continue
        plants_rarity[plant]["ratings"].append(float(rating))


    elif current_command == "Update":
        plant, new_rarity = second_command_for_split.split(" - ")
        if plant not in plants_rarity.keys():
            print("error")
            continue
        plants_rarity[plant]["rarity"] = int(new_rarity)

    elif current_command == "Reset":
        if second_command_for_split not in plants_rarity.keys():
            print("error")
            continue
        plants_rarity[second_command_for_split]["ratings"].clear()

print("Plants for the exhibition:")
for plant, data in plants_rarity.items():
    average_rating = sum(data["ratings"]) / len(data["ratings"]) if data["ratings"] else 0.00
    print(f"- {plant}; Rarity: {data['rarity']}; Rating: {average_rating:.2f}")
