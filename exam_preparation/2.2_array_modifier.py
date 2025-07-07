def swap_func(ind_1, ind_2, array_list):
    array_list[ind_1], array_list[ind_2] = array_list[ind_2], array_list[ind_1]
    return array_list

def mult_func(ind_1, ind_2, array_list):
    new_el = array_list[ind_1] * array_list[ind_2]
    array_list[ind_1] = new_el
    return array_list

def decrease_func(array_list):
    for num in range(len(array_list)):
        array_list[num] -= 1
    return array_list

array = [int(num) for num in input().split()]

while True:
    command = input().split()

    if command [0] == "end":
        break
    elif command[0] == "swap":
        first_ind = int(command[1])
        second_ind = int(command[2])
        result = swap_func(first_ind, second_ind, array)

    elif command[0] == "multiply":
        first_ind = int(command[1])
        second_ind = int(command[2])
        result = mult_func(first_ind, second_ind, array)

    elif command[0] == "decrease":
        result = decrease_func(array)


print(", ".join(str(n) for n in array))