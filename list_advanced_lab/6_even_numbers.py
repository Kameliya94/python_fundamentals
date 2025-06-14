string_of_numbers = input().split(", ")
int_of_numbers = [int(num) for num in string_of_numbers]
even_indices = [num for num in range(len(int_of_numbers)) if int_of_numbers[num] % 2 == 0]
print(even_indices)