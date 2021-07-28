class School:
    def __init__(self):
        self.data = []

    def add_student(self, name, grade):
        self.data.append({"Name": name, "Grade": grade})
        self.data = sorted(self.data, key=lambda k: (k["Grade"], k["Name"]))

    def roster(self):
        l_data = [k["Name"] for k in self.data]
        return l_data

    def grade(self, grade_number):
        l_data = [k["Name"] for k in self.data if k["Grade"] == grade_number]
        return l_data
