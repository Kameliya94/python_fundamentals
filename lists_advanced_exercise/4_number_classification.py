numbers = [int(digit) for digit in input().split(", ")]
positive_numbers = [digit for digit in numbers if digit >= 0]
negative_numbers = [digit for digit in numbers if digit < 0]
even_numbers = [digit for digit in numbers if digit % 2 == 0]
odd_numbers = [digit for digit in numbers if digit % 2 != 0]

print(f"Positive: {', '.join(str(digit) for digit in positive_numbers)}"
      f"\nNegative: {', '.join(str(digit) for digit in negative_numbers)}"
      f"\nEven: {', '.join(str(digit) for digit in even_numbers)}"
      f"\nOdd: {', '.join(str(digit) for digit in odd_numbers)}")