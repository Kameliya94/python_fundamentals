class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals_list = []
        self.fishes_list = []
        self.birds_list = []


    def add_animals(self,species, name):
        if species == "mammal":
            self.mammals_list.append(name)
        elif species == "fish":
            self.fishes_list.append(name)
        elif species == "bird":
            self.birds_list.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == "mammal":
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals_list)}\n"
        elif species == "fish":
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes_list)}\n"
        if species == "bird":
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds_list)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result

zoo_name = input()
zoo = Zoo(zoo_name)
number = int(input())

for num in range(number):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.add_animals(species, name)

info = input()
print(zoo.get_info(info))
