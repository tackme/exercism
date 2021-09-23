def is_paired(input_string: str) -> bool:
    pairs = {'{': '}', '[': ']', '(': ')'}
    opener = pairs.keys()
    closer = pairs.values()

    stack = []
    for char in input_string:
        if char in opener:
            stack.append(char)
        elif char in closer:
            if not stack or pairs[stack.pop()] != char:
                return False

    return not stack
