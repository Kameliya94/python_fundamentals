string = input()
last_letter = ''
result = ''

for char in string:
    if char != last_letter:
        result += char
    last_letter = char

print(result)