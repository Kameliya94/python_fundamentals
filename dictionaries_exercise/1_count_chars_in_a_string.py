string = input()
count = {}

for char in string:
    if char == " ":
        continue

    if char not in count.keys():
        count[char] = 1
    else:
        count[char] += 1

for key, value in count.items():
    print(f"{key} -> {value}")