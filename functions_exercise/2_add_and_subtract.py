def sum_numbers(num1, num2):
    return num1 + num2


def subtract(result, num3):
    return result - num3


def add_and_subtract(num1, num2, num3):
    sum_of_numbers = sum_numbers(num1, num2)
    sum_of_subtract_numbers = subtract(sum_of_numbers, num3)
    return sum_of_subtract_numbers


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))