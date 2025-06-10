group_size = int(input())
days = int(input())
coins = 0

for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5

    coins += 50 - (group_size * 2)

    if current_day % 3 == 0:
        if current_day % 5 == 0:
            coins -= (group_size * 5)
        else:
            coins -= (group_size * 3)

    if current_day % 5 == 0:
        coins += (20 * group_size)

print(f"{group_size} companions received {coins // group_size} coins each.")
