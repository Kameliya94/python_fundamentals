budget = int(input())
command = input()

while command != "End":
    if budget < int(command):
        print("You went in overdraft!")
        break

    budget -= int(command)

    command = input()
else:
    print("You bought everything needed.")
