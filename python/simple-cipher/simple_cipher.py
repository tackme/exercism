from operator import add, sub
from itertools import cycle
from string import ascii_lowercase
from random import choices
from typing import Callable


class Cipher:
    def __init__(self, key: str = None):
        if key is None:
            self.key = "".join(choices(ascii_lowercase, k=100))
        else:
            self.key = key

    def cyclic_shift(self, text: str, op: Callable[[int, int], int]) -> str:
        result = []

        for char1, char2 in zip(text, cycle(self.key[0:len(text)])):
            result.append(ascii_lowercase[op(self.get_index(char1), self.get_index(char2)) % 26])

        return "".join(result)

    def encode(self, text: str) -> str:
        return self.cyclic_shift(text, add)


    def decode(self, text: str) -> str:
        return self.cyclic_shift(text, sub)


    @staticmethod
    def get_index(char: str) -> int:
        return ascii_lowercase.index(char)
