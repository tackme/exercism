from typing import Callable, Iterable, List, Optional, Tuple, Union
from operator import gt, lt

def is_palindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]


def check_factors(min_factor: int, max_factor: int):
    if min_factor > max_factor:
        raise ValueError("min_factor must be smaller than max_factor.")


def find_palindrome(product: int, rng: Iterable[int], op: Callable[[int, int], bool]) -> Tuple[int, List[List[int]]]:
    factors = []

    for i in rng:
        for j in rng:
            n = i * j

            if op(product, n):
                break

            if is_palindrome(n):
                if op(n, product):
                    product = n
                    factors = [sorted((i, j))]
                elif product == n:
                    factors.append(sorted((i, j)))

    return product, factors


def largest(min_factor: int, max_factor: int) -> List[Union[Optional[int], List[List[int]]]]:
    check_factors(min_factor, max_factor)

    product, factors = find_palindrome(0, range(max_factor, min_factor - 1, -1), gt)


    return [product or None, factors]

def smallest(min_factor: int, max_factor: int) -> List[Union[Optional[int], List[List[int]]]]:
    check_factors(min_factor, max_factor)

    product, factors = find_palindrome(max_factor ** 2, range(min_factor, max_factor + 1), lt)

    return [product if is_palindrome(product) else None, factors]
