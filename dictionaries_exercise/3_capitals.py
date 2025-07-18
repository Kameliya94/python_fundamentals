country = input().split(", ")
city = input().split(", ")

new_dict = {country[index]:city[index] for index in range(len(country))}

for key,value in new_dict.items():
    print(f"{key} -> {value}")
