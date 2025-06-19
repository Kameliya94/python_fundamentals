number_of_room = int(input())
free_chairs = 0

for room in range(1, number_of_room + 1):
    chairs_and_people = input().split()
    chairs = len(chairs_and_people[0])
    people = int(chairs_and_people[1])
    difference = chairs - people
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {room}")
    free_chairs += difference

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")