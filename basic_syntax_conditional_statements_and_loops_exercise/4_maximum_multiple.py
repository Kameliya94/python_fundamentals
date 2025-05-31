divisor = int(input())
boundary = int(input())
result = 0

for number in range (boundary, 1, -1):
    if number % divisor == 0:
        result = number
        break
print(result)