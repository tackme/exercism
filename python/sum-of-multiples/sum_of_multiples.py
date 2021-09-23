from typing import List

def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    result = []

    for number in multiples:
        for i in range(1, limit):
            if number * i >= limit:
                break
            result.append(number * i)

    return sum(set(result))
