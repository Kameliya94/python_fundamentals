age = int(input())
result = ''

if age <= 14:
    result = "toddy"
elif age <= 18:
    result = "coke"
elif age <= 21:
    result = "beer"
elif age > 21:
    result = "whisky"

print(f"drink {result}")