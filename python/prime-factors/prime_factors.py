from typing import List


def factors(value: int) -> List[int]:
    result = []
    while value % 2 == 0:
        result.append(2)
        value //= 2
    f = 3
    while f * f <= value:
        if value % f == 0:
            result.append(f)
            value //= f
        else:
            f += 2
    if value != 1:
        result.append(value)
    return result
