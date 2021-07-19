class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(num) for num in item.split(" ")] for item in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        column = [item[index-1] for item in self.matrix]

        return column
