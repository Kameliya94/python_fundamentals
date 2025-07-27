dict_students = {}
number_of_commands = int(input())

for command in range(number_of_commands):
    student = input()
    grade = float(input())

    if student not in dict_students:
        dict_students[student] = []

    dict_students[student].append(grade)

for student, grade in dict_students.items():
    average_grade = (sum(grade) / len(grade))
    if average_grade >= 4.50:
     print(f"{student} -> {average_grade:.2f}")