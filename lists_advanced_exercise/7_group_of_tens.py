numbers = [int(digit) for digit in input().split(", ")]
min_group_of_numbers = 0
max_group_of_numbers = 10

while numbers:
    valid_numbers = [num for num in numbers if min_group_of_numbers < num <= max_group_of_numbers]
    print(f"Group of {max_group_of_numbers}'s: {valid_numbers}")
    numbers = [num for num in numbers if not (min_group_of_numbers < num <= max_group_of_numbers)]
    min_group_of_numbers += 10
    max_group_of_numbers += 10





