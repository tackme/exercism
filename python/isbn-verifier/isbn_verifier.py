import re

def is_valid(isbn):
    numbers = isbn.replace('-', '')

    # Validate isbn
    if not re.fullmatch(r"[0-9]{9}[0-9X]", numbers):
        return False

    num_list = list(numbers)

    # Convert X to 10
    if num_list[-1] == 'X':
        num_list[-1] = '10'

    # Return bool
    return sum(int(l) * (10 - index) for index, l in enumerate(num_list)) % 11 == 0
