first_sequences = input().split(", ")
second_sequences = input().split(", ")
new_list = []

for word in first_sequences:
    for second_word in second_sequences:
        if word in second_word:
            new_list.append(word)
            break

print(new_list)
