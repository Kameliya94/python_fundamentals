students = []
course_to_search = ''

while True:
    students_info = input()

    if ":" not in students_info:
        course_to_search = students_info
        break

    name, student_id, course = students_info.split(":")
    students.append({'name': name, 'ID': student_id, 'course': course})

for student in students:
    if course_to_search.startswith(student['course'][0:4]):
        print(f"{student['name']} - {student['ID']}")