# Score categories.
# Change the values as you see fit.
YACHT = lambda x: 50 if len(set(x)) == 1 else 0
ONES = lambda x: sum(l for l in x if l == 1)
TWOS = lambda x: sum(l for l in x if l == 2)
THREES = lambda x: sum(l for l in x if l == 3)
FOURS = lambda x: sum(l for l in x if l == 4)
FIVES = lambda x: sum(l for l in x if l == 5)
SIXES = lambda x: sum(l for l in x if l == 6)
FULL_HOUSE = lambda x: sum(x) if len(set(x)) == 2 and any(x.count(l) == 3 for l in x) else 0
FOUR_OF_A_KIND = lambda x: sum(l * 4 for l in set(x) if x.count(l) > 3)
LITTLE_STRAIGHT = lambda x: 30 if sorted(x) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda x: 30 if sorted(x) == [2, 3, 4, 5, 6] else 0
CHOICE = sum


def score(dice, category):
    return category(dice)
