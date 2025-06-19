username = input()


while True:
    command = input().split()
    new_username = ""
    if command[0] == "Registration":
        break

    elif command[0] == "Letters":
        if command[1] == "Lower":
            username = username.lower()
            print(username)
        elif command[1] == "Upper":
            username = username.upper()
            print(username)
    elif command [0] == "Reverse":
        start_index,end_index = int(command[1]), int(command[2]) + 1
        if not 0 <= start_index < len(username) or not 0 <= end_index - 1 < len(username):
            continue
        else:
            part_for_reverse = username[start_index: end_index]
            new_username = part_for_reverse[::-1]
            print(new_username)
    elif command[0] == "Substring":
        substring = command[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif command[0] == "Replace":
        char = command[1]
        username = username.replace(char,"-")
        print(username)
    elif command[0] == "IsValid":
         valid_char = command[1]
         if valid_char in username:
             print("Valid username.")
         else:
             print(f"{valid_char} must be contained in your username.")