number_one = int(input())
number_two = int(input())
number_three = int(input())

largest_number = 0

if number_one > number_two and number_one > number_three:
    largest_number = number_one
elif number_two > number_one and number_two > number_three:
    largest_number = number_two
elif number_three > number_two and number_three > number_one:
    largest_number = number_three

print(largest_number)