def sort_numbers(number: list[int]):
    return sorted(number)



numbers_as_str = input().split()
numbers_as_digits = []
for num in numbers_as_str:
    numbers_as_digits.append(int(num))

print(sort_numbers(numbers_as_digits))

