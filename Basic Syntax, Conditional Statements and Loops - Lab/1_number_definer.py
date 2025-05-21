number = float(input())
result = ''

if number == 0:
    result = "zero"
elif number > 0:
    result = "positive"
    if  0 < number < 1:
        result = "small positive"
    elif number > 1000000:
        result = "large positive"

elif number < 0:
    result = "negative"
    if  0 > number > -1:
        result = "small negative"
    elif number < -1000000:
        result = "large negative"

print(result)