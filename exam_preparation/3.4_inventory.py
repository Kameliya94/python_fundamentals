items = input().split(", ")

while True:
    command = input().split(" - ")

    if command[0] == "Craft!":
        print(", ".join(items))
        break

    if command[0] == "Collect":
        new_item = command[1]
        if new_item not in items:
            items.append(new_item)
        else:
            continue

    if command[0] == "Drop":
        new_item = command[1]
        if new_item in items:
            items.remove(new_item)

    if command[0] == "Combine Items":
        new_list = command[1].split(":")
        old_item = new_list[0]
        new_item = new_list[1]

        if old_item in items:
            index = items.index(old_item)
            items.insert(index + 1, new_item)

    if command[0] == "Renew":
        new_item = command[1]
        if new_item in items:
            items.remove(new_item)
            items.append(new_item)