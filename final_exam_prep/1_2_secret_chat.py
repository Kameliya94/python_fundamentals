message = input()

while (command := input()) != "Reveal":
    current_command = command.split(":|:")

    if current_command[0] == "InsertSpace":
        index = int(current_command[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif current_command[0] == "Reverse":
        substring = current_command[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            new_substring = substring[::-1]
            message = message + new_substring
            print(message)
        else:
            print("error")

    elif current_command[0] == "ChangeAll":
        substring = current_command[1]
        replacement =  current_command[2]
        message = message.replace(substring, replacement)
        print(message)

print(f"You have a new text message: {message}")