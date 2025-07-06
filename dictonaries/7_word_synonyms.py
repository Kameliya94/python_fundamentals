dict_synonyms = {}
count_of_words = int(input())

for word in range(count_of_words):
    new_word = input()
    synonym = input()
    if new_word not in dict_synonyms:
        dict_synonyms[new_word] = []
    dict_synonyms[new_word].append(synonym)

for word in dict_synonyms:
    print(f"{word} - {', '.join(dict_synonyms[word])}")