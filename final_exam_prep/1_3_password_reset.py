password = input()


while (command := input()) != "Done":
    current_command = command.split()

    if current_command[0] == "TakeOdd":
        counter = -1
        new_password = ""
        for char in password:
            counter += 1
            if counter % 2 != 0:
                new_password += char
        password = new_password
        print(password)

    elif current_command[0] == "Cut":
        index = int(current_command[1])
        length = int(current_command[2])
        substring = password[index:index+length]
        password = password.replace(substring, "", 1)
        print(password)

    elif current_command[0] == "Substitute":
        substring = current_command[1]
        substitute = current_command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")