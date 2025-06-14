words = input().split()
palindrome = input()

palindromes_in_words = [word for word in words if word == word[::-1]]
counter_palindrome = palindromes_in_words.count(palindrome)

print(palindromes_in_words)
print(f"Found palindrome {counter_palindrome} times")