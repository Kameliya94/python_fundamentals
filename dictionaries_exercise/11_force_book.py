force_dict = {}

while (command := input()) != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        force_user_found = False

        for list_of_force_users in force_dict.values():
            if force_user in list_of_force_users:
                force_user_found = True
                break
        if not force_user_found:
            if force_side not in force_dict:
                force_dict[force_side] = []
            force_dict[force_side].append(force_user)

    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for list_of_force_users in force_dict.values():
            if force_user in list_of_force_users:
                list_of_force_users.remove(force_user)
                break
        if force_side not in force_dict.keys():
            force_dict[force_side] = []
        force_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for force_side, list_of_force_users in force_dict.items():
    if list_of_force_users:
        print(f"Side: {force_side}, Members: {len(list_of_force_users)}")
        for force_user in list_of_force_users:
            print(f"! {force_user}")