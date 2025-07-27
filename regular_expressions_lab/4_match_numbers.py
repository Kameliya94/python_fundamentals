import re

numbers = input()
pattern = r"(?<![\w.-])\-?\d+(?:\.\d+)?(?![\w.])"
valid_numbers = re.findall(pattern, numbers)

print(" ".join(valid_numbers))