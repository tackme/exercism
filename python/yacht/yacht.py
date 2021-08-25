from collections import Counter

# Score categories.
# Change the values as you see fit.

YACHT = lambda x: 50 if len(x) == 1 else 0
ONES = lambda x: x[1]
TWOS = lambda x: x[2] * 2
THREES = lambda x: x[3] * 3
FOURS = lambda x: x[4] * 4
FIVES = lambda x: x[5] * 5
SIXES = lambda x: x[6] * 6
FULL_HOUSE = lambda x: sum(k * v for k, v in x.items()) if len(x) == 2 and 3 in x.values() else 0
FOUR_OF_A_KIND = lambda x: max(x) * 4 if max(x.values()) > 3 else 0
LITTLE_STRAIGHT = lambda x: 30 if sum(x.keys()) == 15 else 0
BIG_STRAIGHT = lambda x: 30 if sum(x.keys()) == 20 else 0
CHOICE = lambda x: sum(k * v for k, v in x.items())

def score(dice, category):
    dice_counter = Counter(dice)

    return category(dice_counter)
