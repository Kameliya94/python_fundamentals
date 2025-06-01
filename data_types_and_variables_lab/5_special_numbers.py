number = int(input())

for current_number in range(1, number + 1):
    current_number_str = str(current_number)
    sum_of_digits = 0
    for current_digit in current_number_str:
        sum_of_digits += int(current_digit)
    is_special = False

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        is_special = True

    print(f"{current_number} -> {is_special}")

