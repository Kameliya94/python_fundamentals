empl_1 = int(input())
empl_2 = int(input())
empl_3 = int(input())
students = int(input())

work_done_for_hour = empl_1 + empl_2 + empl_3
needed_time = 0

while students > 0:
    needed_time += 1
    if needed_time % 4 == 0:
        continue
    students -= work_done_for_hour

print(f"Time needed: {needed_time}h.")