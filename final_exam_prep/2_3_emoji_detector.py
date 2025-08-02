import re

cool_threshold = 1
emojis = 0
emojis_list = []

text = input()

pattern_for_coolness = r"[\d]"
pattern_for_emojis = r"(\:\:|\*\*)([A-Z][a-z]{2,})\1"

matches_for_coolness = re.findall(pattern_for_coolness, text)
matches_for_emoji = re.finditer(pattern_for_emojis, text)

for match in matches_for_coolness:
    cool_threshold *= int(match)

for match in matches_for_emoji:
    emojis += 1
    emojis_text = match.group(2)
    emoji_coolness = sum(ord(char) for char in emojis_text)
    if emoji_coolness >= cool_threshold:
        emojis_list.append(match.group(0))

print(f'Cool threshold: {cool_threshold}')
print(f"{emojis} emojis found in the text. The cool ones are:")
print("\n".join(emojis_list))