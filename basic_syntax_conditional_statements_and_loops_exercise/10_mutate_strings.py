string_one = input()
string_two = input()
last_printed_string = string_one

for char in range(len(string_one)):
    left_part = string_two [:char +1]
    right_part = string_one [char + 1:]
    new_string = left_part + right_part

    if new_string != last_printed_string:
        print(new_string)
        last_printed_string = new_string