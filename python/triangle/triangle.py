from typing import List


def is_triangle(sides: List[int]) -> bool:
    return max(sides) < (sum(sides) - max(sides))


def equilateral(sides: List[int]) -> bool:
    return len(set(sides)) == 1 and is_triangle(sides)


def isosceles(sides: List[int]) -> bool:
    return len(set(sides)) <= 2 and is_triangle(sides)


def scalene(sides: List[int]) -> bool:
    return len(set(sides)) == 3 and is_triangle(sides)
