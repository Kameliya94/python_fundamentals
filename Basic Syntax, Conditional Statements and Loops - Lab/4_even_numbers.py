n = int(input())
result = ''

for _ in range (n):
    number = int(input())
    if number % 2 != 0:
        result = f"{number} is odd!"
        break
    else:
        result = "All numbers are even."

print(result)