import string
import random

class Robot:
    def __init__(self):
        self.generate_name()

    def generate_name(self):
        random.seed()

        random_letters = "".join(random.choices(string.ascii_uppercase, k=2))
        random_numbers = str(random.randrange(100, 1000))

        self.name = random_letters + random_numbers

    def reset(self):
        self.__init__()
