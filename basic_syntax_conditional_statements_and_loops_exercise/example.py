command = input()
coffee = 0

while command != "END":

    if (command == "coding" or command == "dog"
            or command == "cat" or command == "movie"):
        if command.isupper:
            coffee += 2
        else:
            coffee += 1

    command = input()

else:
    if coffee > 5:
        print("You need extra sleep")
    else:
        print(f"{coffee}")

