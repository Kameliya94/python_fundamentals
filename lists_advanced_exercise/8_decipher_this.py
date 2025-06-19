def decipher_message(message):
    deciphered_message = []
    for word in message:
        word = [char for char in word]
        number_as_string = ""
        for index in range(len(word)):
            if word[index].isdigit():
                number_as_string += word[index]
            else:
                break
        digits_as_letter = chr(int(number_as_string))
        word_with_letters = word[index:]
        word_with_letters[0], word_with_letters[-1] = word_with_letters[-1], word_with_letters[0]
        decipher_word = digits_as_letter + "".join(word_with_letters)
        deciphered_message.append(decipher_word)

    return deciphered_message


secret_message = input().split()
result = decipher_message(secret_message)
print(" ".join(result))