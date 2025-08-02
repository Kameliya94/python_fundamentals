import re

string = input()
mirror_words = []
count = 0

pattern = r"([@#])(?P<word1>[A-Za-z]{3,})\1\1(?P<word2>[A-Za-z]{3,})\1"
matches = re.finditer(pattern, string)


for match in matches:
    count += 1
    word_one = match.group("word1")
    word_two = match.group("word2")
    if word_one == word_two[::-1]:
        mirror_words.append(f"{word_one} <=> {word_two}")

if count == 0:
    print("No word pairs found!")
else:
    print(f"{count} word pairs found!")

if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))