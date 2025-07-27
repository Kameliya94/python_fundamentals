courses_dict = {}

while (command := input()) != "end":
    course, student = command.split(" : ")

    if course not in courses_dict.keys():
        courses_dict[course] = []

    courses_dict[course].append(student)

for course,students in courses_dict.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")