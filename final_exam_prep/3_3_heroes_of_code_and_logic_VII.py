hero_dict = {}

n = int(input())
for _ in range(n):
    hero, hp, mp = input().split()
    hero_dict[hero] = {"HP": int(hp), "MP": int(mp)}

while True:
    command = input().split(" - ")

    if command[0] == "End":
        break

    if command[0] == "CastSpell":
        hero = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]

        if mp_needed <= hero_dict[hero]["MP"]:
            hero_dict[hero]["MP"] -= mp_needed
            print(f'{hero} has successfully cast {spell_name} and now has {hero_dict[hero]["MP"]} MP!')
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif command[0] == "TakeDamage":
        hero = command[1]
        damage = int(command[2])
        attacker = command[3]

        hero_dict[hero]["HP"] -= damage

        if hero_dict[hero]["HP"] > 0:
            print(f'{hero} was hit for {damage} HP by {attacker} and now has {hero_dict[hero]["HP"]} HP left!')
        else:
            print(f"{hero} has been killed by {attacker}!")

    elif command[0] == "Recharge":
        hero = command[1]
        amount = int(command[2])

        recoverable = 200 - hero_dict[hero]["MP"]
        to_add = min(amount, recoverable)
        hero_dict[hero]["MP"] += to_add
        print(f"{hero} recharged for {to_add} MP!")

    elif command[0] == "Heal":
        hero = command[1]
        amount = int(command[2])

        recoverable = 100 - hero_dict[hero]["HP"]
        to_add = min(amount, recoverable)
        hero_dict[hero]["HP"] += to_add
        print(f"{hero} healed for {to_add} HP!")



for hero, data in hero_dict.items():
    if data["HP"] > 0:
        print(f'{hero}\n HP: {data["HP"]}\n MP: {data["MP"]}')