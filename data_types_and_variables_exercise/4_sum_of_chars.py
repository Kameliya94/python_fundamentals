n = int(input())
total_sum = 0

for character in range(n):
    curr_character = input()
    total_sum += ord(curr_character)

print(f"The sum equals: {total_sum}")
