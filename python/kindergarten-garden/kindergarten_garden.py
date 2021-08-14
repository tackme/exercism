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
        chunked_garden = [chunked(l, 2) for l in garden]
        self.transeposed = [list(l) for l in zip(*chunked_garden)]
        self.students = sorted(students)

    def plants(self, name):
        index = self.students.index(name)

        flatten_garden = sum(self.transeposed[index], [])

        return list(map(self.PLANTS.get, flatten_garden))
