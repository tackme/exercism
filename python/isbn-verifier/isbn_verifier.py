def is_valid(isbn):
    # Make number list(with alphabet)
    numbers = list(isbn.replace('-', ''))

    # Exclude wrong length list
    if len(numbers) != 10:
        return False

    # Convert X to 10
    if numbers[-1] == 'X':
        numbers[-1] = '10'

    # Return bool (with exception)
    try:
        return sum(int(l) * (10 - index) for index, l in enumerate(numbers)) % 11 == 0
    except ValueError:
        return False
