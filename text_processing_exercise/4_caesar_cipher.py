string = input()
encrypted_text = ''

for char in string:
    encrypted_text += chr(ord(char) + 3)

print(encrypted_text)