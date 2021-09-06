def steps(number):
    if number <= 0:
        raise ValueError("number should be greater than 0")

    total_steps = 0

    while number != 1:
        if number % 2 == 0:
            number = number / 2
            total_steps += 1
        else:
            number = number * 3 + 1
            total_steps += 1


    return total_steps
