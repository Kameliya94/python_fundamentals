def sorted_numbers (number: list[int]):
    min_number = min(number)
    max_number = max(number)
    sum_of_numbers = sum(number)
    return f"The minimum number is {min_number}\n The maximum number is {max_number}\n The sum number is: {sum_of_numbers}"

numbers_as_str = input().split()
numbers_as_digits = []
for num in numbers_as_str:
    numbers_as_digits.append(int(num))

print(sorted_numbers(numbers_as_digits))

