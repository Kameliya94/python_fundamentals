text = input().split()
new_text = [word for word in text if len(word) % 2 == 0]

print("\n".join(new_text))