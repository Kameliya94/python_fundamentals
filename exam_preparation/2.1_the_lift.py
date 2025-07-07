MAX_PEOPLE_IN_WAGON = 4

people = int(input())
wagons = [int(num) for num in input().split()]

for i in range(len(wagons)):
    available_space = MAX_PEOPLE_IN_WAGON - wagons[i]
    people_to_add = min(available_space, people)
    wagons[i] += people_to_add
    people -= people_to_add

if people == 0 and len(list(filter(lambda w: w < MAX_PEOPLE_IN_WAGON, wagons))) > 0:
    print("The lift has empty spots!")
elif people > 0 and len(list(filter(lambda w: w == MAX_PEOPLE_IN_WAGON, wagons))) == len(wagons):
    print(f"There isn't enough space! {people} people in a queue!")

print(" ".join(str(w) for w in wagons))