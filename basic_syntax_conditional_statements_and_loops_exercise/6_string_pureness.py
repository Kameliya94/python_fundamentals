number = int(input())

for string in range(number):
    command = input()

    if ("." in command
            or "," in command
            or "_" in command):
        print(f"{command} is not pure!")
    else:
        print(f"{command} is pure.")