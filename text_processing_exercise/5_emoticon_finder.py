string = input()
emoticon = ''

for index in range (len(string)):
    if string[index] == ":":
        emoticon = string[index] + string[index + 1]
        print(emoticon)