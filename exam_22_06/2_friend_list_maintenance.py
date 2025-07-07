def blacklist_func(name_: str, friends_list: list):
    if name_ in friends_list:
        print(f"{name_} was blacklisted.")
        ind_name = friends_list.index(name_)
        friends_list[ind_name] = "Blacklisted"
    else:
        print(f"{name_} was not found.")
    return friends_list

def error_func(ind: int, friends_list:list):
    if ind >= 0 and not ind > len(friends_list) - 1:
        if friends_list[ind] != "Blacklisted" and friends_list[ind] != "Lost":
            print(f"{friends_list[ind]} was lost due to an error.")
            friends_list[ind] = "Lost"
    return friends_list

def change_func(ind: int, new_name_: str, friends_list: list):
    if ind >= 0 and not ind > len(friends_list) - 1:
        print(f"{friends_list[ind]} changed his username to {new_name_}.")
        friends_list[ind] = new_name_
    return friends_list

friends = input().split(", ")

while True:
    command = input().split()

    if command[0] == "Report":
        print(f"Blacklisted names: {friends.count('Blacklisted')}"
              f"\nLost names: {friends.count('Lost')}")
        print(" ".join(friends))
        break

    elif command [0] == "Blacklist":
        name = command[1]
        blacklist_func(name, friends)

    elif command[0] == "Error":
        index = int(command[1])
        error_func(index, friends)

    elif command[0] == "Change":
        index = int(command[1])
        new_name = command[2]
        change_func(index, new_name, friends)