number_of_commands = int(input())
registered_cars = {}

for command in range(number_of_commands):
    data = input().split()

    if data[0] == "register":
        if data[1] in registered_cars:
            print(f"ERROR: already registered with plate number {registered_cars[data[1]]}")
        else:
            registered_cars[data[1]] = data[2]
            print(f"{data[1]} registered {data[2]} successfully")

    elif data[0] == "unregister":
        if data[1] not in registered_cars.keys():
            print(f"ERROR: user {data[1]} not found")
        else:
            del registered_cars[data[1]]
            print(f"{data[1]} unregistered successfully")

for username, license_plate_number in registered_cars.items():
    print(f"{username} => {license_plate_number}")