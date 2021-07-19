class Matrix:
    def __init__(self, matrix_string):
        matrix_string = matrix_string.splitlines()

        self.matrix = []

        for item in matrix_string:
            nums = item.split(" ")
            row_int =[]
            for num in nums:
                row_int.append(int(num))
            self.matrix.append(row_int)

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        column = []

        for item in self.matrix:
            column.append(item[index-1])

        return column
