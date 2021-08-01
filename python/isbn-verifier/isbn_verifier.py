import re

def is_valid(isbn):
    numbers = list(isbn.replace('-', ''))

    # Validate isbn
    if not re.fullmatch(r"[0-9]{9}[0-9X]", numbers):
        return False

    # Convert X to 10
    if numbers[-1] == 'X':
        numbers[-1] = '10'

    # Return bool
    return sum(int(l) * (10 - index) for index, l in enumerate(numbers)) % 11 == 0
