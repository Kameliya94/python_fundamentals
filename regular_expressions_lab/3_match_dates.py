import re

dates = input()

pattern = r'(\d{2})([-./])([A-z][a-z]{2})\2(\d{4})'

matches = re.findall(pattern, dates)

for date in matches:
    day = date[0]
    month = date[2]
    year = date[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")