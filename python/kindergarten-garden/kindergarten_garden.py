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
        self.garden = [list(l) for l in diagram.split()]
        self.students = sorted(students)

    def plants(self, name):
        index = self.students.index(name) * 2

        pots = self.garden[0][index:index+2] + self.garden[1][index:index+2]

        return [self.PLANTS[l] for l in pots]
