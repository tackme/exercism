class School:
    def __init__(self):
        self._data = []

    def add_student(self, name, grade):
        self._data.append({"Name": name, "Grade": grade})
        self._data = sorted(self._data, key=lambda x: (x["Grade"], x["Name"]))

    def roster(self):
        names = [d["Name"] for d in self._data]
        return names

    def grade(self, grade_number):
        names = [d["Name"] for d in self._data if d["Grade"] == grade_number]
        return names
