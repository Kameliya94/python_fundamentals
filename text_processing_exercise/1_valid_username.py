def valid_length(current_username):
    if 3 <= len(current_username) <= 16:
        return True
    return False

def valid_char(current_username):
    for character in current_username:
        if not(character.isalnum() or character == "-" or character == "_"):
            return False
    return True

def no_redundant_symbols(current_username):
    if " " in current_username:
        return False
    return True

def valid_username(current_username):
    if (valid_length(current_username)
            and valid_char(current_username)
            and no_redundant_symbols(current_username)):
        return True
    return False

usernames = input().split(", ")

for username in usernames:
    if valid_username(username):
        print(username)