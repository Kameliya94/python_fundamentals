phonebook = {}

while True:
    command = input()
    if command.isdigit():
        number_of_search = int(command)
        break

    name, phone = command.split("-")
    phonebook[name] = phone

for search in range(number_of_search):
    name = input()

    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")