def factorial_division(num1: int):
    for digit in range(1, num1):
        num1 *= digit

    return num1

first_number = int(input())
second_number = int(input())
first_number_calculated = factorial_division(first_number)
second_number_calculated = factorial_division(second_number)

print(f"{first_number_calculated / second_number_calculated:.2f}")