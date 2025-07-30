import re

text = input()

pattern = r"([#|])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"

matches = list(re.finditer(pattern, text))

total_calories = 0

for match in matches:
    calories = int(match.group(4))
    total_calories += calories

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")

for match in matches:
    item = match.group(2)
    date = match.group(3)
    calories = int(match.group(4))
    print(f"Item: {item}, Best before: {date}, Nutrition: {calories}")
