gifts = input().split()

while (command := input()) != "No Money":
    command = command.split()
    if command[0] == "OutOfStock":
        for index in range(len(gifts)):
            if gifts[index] == command[1]:
                gifts[index] = "None"

    elif command[0] == "Required":
        gift = command[1]
        index_gift = int(command[2])
        if  0 <= index_gift < len(gifts):
            gifts[index_gift] = gift

    elif command[0] == "JustInCase":
        gift = command[1]
        gifts[-1] = gift

print(" ".join(gift for gift in gifts if gift != "None"))