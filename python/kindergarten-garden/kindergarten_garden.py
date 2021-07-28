class Garden:
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
        self.diagram = diagram.split()
        self.students = sorted(students)

    def plants(self, name):
        ref = {
            "G" : "Grass",
            "C" : "Clover",
            "R" : "Radishes",
            "V" : "Violets"
            }

        index = self.students.index(name) * 2

        reslut = [ref[m] for l in self.diagram for m in l[index:index+2]]

        return reslut
