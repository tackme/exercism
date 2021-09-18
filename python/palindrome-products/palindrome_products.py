from typing import List, Optional, Union

def is_palindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]

def check_factors(min_factor: int, max_factor: int):
    if min_factor > max_factor:
        raise ValueError("min_factor must be smaller than max_factor.")

def largest(min_factor: int, max_factor: int) -> List[Union[Optional[int], List[List[int]]]]:
    check_factors(min_factor, max_factor)

    product = 0
    factors = []

    for i in range(max_factor, min_factor - 1, -1):
        for j in range(max_factor, min_factor - 1, -1):
            n = i * j

            if product > n:
                break

            if is_palindrome(n):
                if product < n:
                    product = n
                    factors = [sorted((i, j))]
                elif product == n:
                    factors.append(sorted((i, j)))


    return [product or None, factors]

def smallest(min_factor: int, max_factor: int) -> List[Union[Optional[int], List[List[int]]]]:
    check_factors(min_factor, max_factor)

    product = max_factor ** 2
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            n = i * j

            if product < n:
                break

            if is_palindrome(n):
                if product > n:
                    product = n
                    factors = [sorted((i, j))]
                elif product == n:
                    factors.append(sorted((i, j)))


    return [product if is_palindrome(product) else None, factors]
