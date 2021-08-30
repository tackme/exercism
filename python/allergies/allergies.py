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
        self.allergens = []

        for i, l in enumerate(ALLERGEN_TABLE):
            if score >> i & 1:
                self.allergens.append(l)
                if i > 6:
                    break

    def allergic_to(self, item):
        return item in self.allergens

    @property
    def lst(self):
        return self.allergens
