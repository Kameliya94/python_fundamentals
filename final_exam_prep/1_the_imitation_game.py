message = input()

while (command := input()) != "Decode":
    parts = command.split("|")

    if parts[0] == "Move":
        num_of_letters = int(parts[1])
        message = message[num_of_letters:] + message[:num_of_letters]

    elif parts[0] == "Insert":
        index = int(parts[1])
        value = parts[2]
        message = message[:index] + value + message[index:]

    elif parts[0] == "ChangeAll":
        substring = parts[1]
        replacement = parts[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")

