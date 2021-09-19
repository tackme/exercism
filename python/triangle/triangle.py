from typing import List


def equilateral(sides: List[int]) -> bool:
    return len(set(sides)) == 1 and max(sides) < (sum(sides) - max(sides))


def isosceles(sides: List[int]) -> bool:
    return len(set(sides)) <= 2 and max(sides) < (sum(sides) - max(sides))


def scalene(sides: List[int]) -> bool:
    return len(set(sides)) == 3 and max(sides) < (sum(sides) - max(sides))
