shot_targets = [int(num) for num in input().split()]
count_targets = 0

while True:
    command = input()

    if command == "End":
        print(f"Shot targets: {count_targets} -> {' '.join(str(x) for x in shot_targets)}")
        break

    else:
        index = int(command)
        if 0 <= index < len(shot_targets) and shot_targets[index] != -1:
            current_value = shot_targets[index]
            shot_targets[index] = -1
            count_targets += 1

            for i in range(len(shot_targets)):
                if shot_targets[i] == -1:
                    continue
                if shot_targets[i] > current_value:
                    shot_targets[i] -= current_value
                else:
                    shot_targets[i] += current_value



