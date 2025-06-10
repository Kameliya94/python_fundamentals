number_of_people = int(input())
capacity_elevator = int(input())
turns = 0

while number_of_people > 0:
    turns += 1
    number_of_people -= capacity_elevator

print(turns)