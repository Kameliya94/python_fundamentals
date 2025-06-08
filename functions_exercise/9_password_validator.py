def is_pass_valid(password: str):
    problems = []
    if len(password) < 6 or len(password) > 10:
        problems.append("Password must be between 6 and 10 characters")

    if not password.isalnum():
        problems.append("Password must consist only of letters and digits")

    digit_counter = 0
    for char in password:
        if char.isdigit():
            digit_counter += 1

    if digit_counter < 2:
        problems.append("Password must have at least 2 digits")

    return problems

current_password = input()
problems_in_pass = is_pass_valid(current_password)
if not problems_in_pass:
    print("Password is valid")
else:
    print("\n".join(problems_in_pass))