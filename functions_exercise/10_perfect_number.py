def perf_number(number: int):
    sum_of_divisors = 0
    for digit in range(1, number):
        if number % digit == 0:
            sum_of_divisors += digit

    if sum_of_divisors == number:
        return "We have a perfect number!"

    return "It's not so perfect."

curr_number = int(input())
print(perf_number(curr_number))