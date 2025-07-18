collected_minerals = {"shards": 0, "fragments": 0, "motes": 0}
crafted_legendary = False

while not crafted_legendary:
    items = input().split()
    for index in range(0, len(items), 2):
        value = int(items[index])
        key = items[index+1].lower()

        if key not in collected_minerals.keys():
            collected_minerals[key] = 0
        collected_minerals[key] += value

        if collected_minerals["shards"] >= 250:
            collected_minerals["shards"] -= 250
            print("Shadowmourne obtained!")
            crafted_legendary = True
        elif collected_minerals["fragments"] >= 250:
            collected_minerals["fragments"] -= 250
            print("Valanyr obtained!")
            crafted_legendary = True
        elif collected_minerals["motes"] >= 250:
            collected_minerals["motes"] -= 250
            print("Dragonwrath obtained!")
            crafted_legendary = True

        if crafted_legendary:
            break

for key, value in collected_minerals.items():
    print(f"{key}: {value}")