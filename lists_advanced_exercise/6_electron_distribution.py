electrons = int(input())
number_of_shell = 0
shells = []

while electrons > 0:
    number_of_shell += 1
    filled_shell = 2 * number_of_shell ** 2
    if electrons >= filled_shell:
        shells.append(filled_shell)
    else:
        shells.append(electrons)
    electrons -= filled_shell

print(shells)