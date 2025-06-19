message = input().split()

while True:
    command = input()

    if command == "3:1":
        break

    new_command = command.split()
    if new_command[0] == "merge":
        start_index = int(new_command[1])
        end_index = int(new_command[2])
        start_index = max(0, start_index)
        end_index = min(len(message) - 1, end_index)
        merged_message  = "".join(message[start_index:end_index + 1])
        del message[start_index:end_index + 1]
        message.insert(start_index, merged_message)

    elif new_command[0] == "divide":
        index = int(new_command[1])
        partitions = int(new_command[2])
        new_element = message[index]
        part_length = len(new_element) // partitions
        remainder_if_not_equal = len(new_element) % partitions
        parts = []

        start = 0
        for i in range(partitions):
            if i == partitions - 1:
                end = start + part_length + remainder_if_not_equal
            else:
                end = start + part_length

            parts.append(new_element[start:end])
            start = end

        del message[index]
        for i, part in enumerate(parts):
            message.insert(index + i, part)

print(" ".join(message))