resources = {}

while (command := input()) != "stop":
    value = int(input())
    if command not in resources.keys():
        resources[command] = 0
    resources[command] += value

for key, value in resources.items():
    print(f"{key} -> {value}")
