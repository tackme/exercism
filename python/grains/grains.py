def square(number):
    if not 0 < number < 65:
        raise ValueError("number's range should be 0 < number < 65")

    return 2 ** (number - 1)


def total():
    return sum([2 ** n for n in range(0, 64)])
