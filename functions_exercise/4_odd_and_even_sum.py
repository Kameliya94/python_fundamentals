def calculate_even_and_odd_digits(number):
    odd_sum = 0
    even_sum = 0

    for digit in number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

current_number = input()
print(calculate_even_and_odd_digits(current_number))