class School:
    def __init__(self):
        self.data = []

    def add_student(self, name, grade):
        self.data.append({"Name": name, "Grade": grade})
        self.data = sorted(self.data, key=lambda x: (x["Grade"], x["Name"]))

    def roster(self):
        names = [d["Name"] for d in self.data]
        return names

    def grade(self, grade_number):
        names = [d["Name"] for d in self.data if d["Grade"] == grade_number]
        return names
