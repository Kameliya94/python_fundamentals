def loading_bar(number: int):
    if number < 100:
        number_for_loaded_bar = number // 10
        return f"{number}% [{'%' * number_for_loaded_bar}{'.' * (10 - number_for_loaded_bar)}]\nStill loading..."
    return f"100% Complete! \n[%%%%%%%%%%]"

percent_loaded_bar = int(input())
print(loading_bar(percent_loaded_bar))

