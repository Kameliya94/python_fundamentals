sequence = [int(num) for num in input().split()]

average_value = sum(sequence) / len(sequence)


new_list = [num for num in sequence if num > average_value]
new_list.sort(reverse=True)

if not new_list:
    print("No")
else:
    print(" ".join(str(num) for num in new_list[:5]))

