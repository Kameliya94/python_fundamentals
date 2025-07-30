collection = {}
n = int(input())

for _ in range(n):
    piece, composer, key = input().split("|")
    collection[piece] = [composer, key]

while (command := input()) != "Stop":
    parts = command.split("|")

    if parts[0] == "Add":
        piece = parts[1]
        composer = parts[2]
        key = parts[3]

        if piece not in collection.keys():
            collection[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif parts[0] == "Remove":
        piece = parts[1]

        if piece in collection.keys():
            del collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif parts[0] == "ChangeKey":
        piece = parts[1]
        new_key = parts[2]

        if piece in collection.keys():
            collection[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, (composer, key) in collection.items():
    print(f"{piece} -> Composer: {composer}, Key: {key}")