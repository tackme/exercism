from more_itertools import chunked

class Garden:
    PLANTS = {
            "G" : "Grass",
            "C" : "Clover",
            "R" : "Radishes",
            "V" : "Violets"
            }

    def __init__(self, diagram, students=None):
        if students is None:
            students = [
                "Alice",
                "Bob",
                "Charlie",
                "David",
                "Eve",
                "Fred",
                "Ginny",
                "Harriet",
                "Ileana",
                "Joseph",
                "Kincaid",
                "Larry"
                ]
        garden = [list(l) for l in diagram.split()]
        self.garden = [list(chunked(l, 2)) for l in garden]
        self.students = sorted(students)

    def plants(self, name):
        index = self.students.index(name)

        pots = self.garden[0][index] + self.garden[1][index]

        return [self.PLANTS[l] for l in pots]
