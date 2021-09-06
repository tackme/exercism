def classify(number):
    if number <= 0:
        raise ValueError("number should be greater than 0")

    # aliquot_sum = sum([i for i in range(1, number) if number % i == 0])
    # too late

    divisors = []
    for i in range(1, int(number**0.5)+1):
        if number % i == 0:
            divisors.append(i)
            if i**2 == number:
                continue
            if number // i != number:
                divisors.append(number//i)

    aliquot_sum = sum(sorted(divisors))

    if aliquot_sum == number and number != 1:
        return "perfect"

    if aliquot_sum > number:
        return "abundant"

    return "deficient"
