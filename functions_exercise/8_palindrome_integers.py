def is_palindrome(number_as_string):
    return number_as_string == number_as_string [::-1]


numbers = input().split(", ")
for current_number_as_string in numbers:
    print(is_palindrome(current_number_as_string))