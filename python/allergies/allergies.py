ALLERGEN_TABLE = [
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats"
        ]

class Allergies:
    def __init__(self, score):
        self.allergens = [ALLERGEN_TABLE[i] for i in range(8) if score >> i & 1]

    def allergic_to(self, item):
        return item in self.allergens

    @property
    def lst(self):
        return self.allergens
