# def even_numbers(number: list[str]):
#     even_list = []
#     for digit in number:
#         if int(digit) % 2 == 0:
#             even_list.append(int(digit))
#     return even_list
#
#
# list_of_numbers = input().split()
# print(even_numbers(list_of_numbers))


def even_numbers(number: int):
    return number % 2 == 0


list_of_numbers_as_string = input().split()
list_of_numbers_as_digits = []
for curr_number in list_of_numbers_as_string:
    list_of_numbers_as_digits.append(int(curr_number))

filtered_items = list(filter(even_numbers, list_of_numbers_as_digits))
print(filtered_items)