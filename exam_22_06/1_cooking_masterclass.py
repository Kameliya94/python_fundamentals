from math import ceil

EGGS_PER_STUDENT = 10
DIRTY_APRON = 0.2

budget = float(input())
students = int(input())
flour = float(input())
eggs = float(input()) * EGGS_PER_STUDENT
apron = float(input())
total_price = 0
price_for_flour = 0
price_for_aprons = (ceil(students * DIRTY_APRON) + students) * apron

for student in range(1, students + 1):
    if student % 5 == 0:
        continue
    price_for_flour += flour

total_price = price_for_flour + (students * eggs) + price_for_aprons

if budget >= total_price:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{total_price - budget:.2f}$ more needed.")