def is_armstrong_number(number):
    digits = len(str(number))

    result = 0

    for n in str(number):
        result += int(n) ** digits

    if number == result:
        return True

    return False
