number_of_snowballs = int(input())
snowball_value = 0
highest_snowball_value = 0
highest_weight_of_snowball = 0
highest_time_needed = 0
highest_quality_snowball = 0

for snowball in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_needed = int(input())
    quality_snowball = int(input())

    snowball_value = int((weight_of_snowball / time_needed) ** quality_snowball)

    if snowball_value > highest_snowball_value:
        highest_snowball_value = snowball_value
        highest_weight_of_snowball = weight_of_snowball
        highest_time_needed = time_needed
        highest_quality_snowball = quality_snowball

print(f"{highest_weight_of_snowball} : {highest_time_needed} = {highest_snowball_value} ({highest_quality_snowball})")