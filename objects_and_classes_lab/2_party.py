class Party:
    def __init__(self):
        self.people = []


party = Party()

while (command:= input()) != "End":
    party.people.append(command)

print(f"Going: {', '.join(party.people)} \nTotal: {len(party.people)}")