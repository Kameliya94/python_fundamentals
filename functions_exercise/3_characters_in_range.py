def char_in_between(char1, char2):
    list_of_char = []
    for index in range(ord(char1) + 1, ord(char2)):
        list_of_char.append(chr(index))
    return list_of_char

char_one = input()
char_two = input()
all_characters = char_in_between(char_one, char_two)
print(" ".join(all_characters))