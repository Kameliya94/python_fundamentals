def shoot_func(ind,power_,targets_list):
    if 0 <= ind < len(targets_list):
        targets_list[ind] -= power_
        if targets_list[ind] <= 0:
            targets_list.pop(ind)
    return targets_list

def add_func(ind,value_,targets_list):
    if 0 <= ind < len(targets_list):
        targets_list.insert(ind, value_)
    else:
        print("Invalid placement!")
    return targets_list

def strike_func(ind,radius_,targets_list):
    start_ind = ind - radius_
    end_ind = ind + radius_

    if start_ind >= 0 and end_ind < len(targets_list):
        del targets_list[start_ind : end_ind + 1]
    else:
        print("Strike missed!")
    return targets_list


targets = [int(num) for num in input().split()]

while True:
    command = input().split()

    if command[0] == "End":
        print("|".join(str(target) for target in targets))
        break

    elif command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])
        shoot_func(index,power,targets)

    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])
        add_func(index,value,targets)

    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        strike_func(index,radius,targets)