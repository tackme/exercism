def get_rounds(number):
    '''

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    '''

    return list(range(number, number + 3))


def concatenate_rounds(rounds_1, rounds_2):
    '''

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    '''

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    '''

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    '''

    return number in rounds


def card_average(hand):
    '''

    :param hand: list - cards in hand.
    :return:  int - average value of the cards in the hand.
    '''

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    '''

    :param hand: list - cards in hand.
    :return: int - approximate average value of the cards in the hand.
    '''

    hand_avg = card_average(hand)

    return hand_avg in [(hand[0] + hand[-1]) // 2, hand[len(hand) // 2]]

def average_even_is_average_odd(hand):
    '''

    :param hand: list - cards in hand.
    :return: int - approximate average value of the cards in the hand.
    '''

    even = hand[0::2]
    odd = hand[1::2]

    return (sum(even) / len(even)) == (sum(odd) / len(odd))

def maybe_double_last(hand):
    '''

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    '''

    if hand[-1] == 11:
        hand[-1] *= 2

    return hand
