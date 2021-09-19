def equilateral(sides):
    return len(set(sides)) == 1 and max(sides) < (sum(sides) - max(sides))


def isosceles(sides):
    return len(set(sides)) <= 2 and max(sides) < (sum(sides) - max(sides))


def scalene(sides):
    return len(set(sides)) == 3 and max(sides) < (sum(sides) - max(sides))
