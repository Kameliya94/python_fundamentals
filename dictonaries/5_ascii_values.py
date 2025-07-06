list_of_char = input().split(", ")

dict_of_char = {char: ord(char) for char in list_of_char}
print(dict_of_char)