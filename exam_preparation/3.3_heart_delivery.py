neighborhood = [int(num) for num in input().split("@")]
last_jump = 0
jump = 0

while True:
    command = input().split()

    if command[0] == "Love!":
        break

    jump += int(command[1])
    if jump > len(neighborhood) - 1:
        jump = 0

    if neighborhood[jump] == 0:
        print(f"Place {jump} already had Valentine's day.")
        last_jump = jump
        continue

    neighborhood[jump] -= 2
    if neighborhood[jump] == 0:
        print(f"Place {jump} has Valentine's day.")

    last_jump = jump

print(f"Cupid's last position was {last_jump}.")


neighborhood = [house for house in neighborhood if house > 0]
if not neighborhood:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood)} places.")