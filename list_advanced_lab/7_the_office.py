def func_for_happiness(employees_happiness_list,factor_happiness):
    multiplied_happiness_by_factor = [happiness * factor for happiness in employees_happiness_list]
    average_happiness = sum(multiplied_happiness_by_factor) / len(employees_happiness_list)
    happy_count = sum(num >= average_happiness for num in multiplied_happiness_by_factor)
    total_count = len(employees_happiness_list)
    is_happy = "happy" if happy_count >= total_count / 2 else "not happy"
    return f"Score: {happy_count}/{total_count}. Employees are {is_happy}!"


employees_happiness = [int(digit) for digit in input().split()]
factor = int(input())
result = func_for_happiness(employees_happiness,factor)
print(result)
