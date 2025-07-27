import re

name = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+"
valid_name = re.findall(pattern, name)

print(" ".join(valid_name))