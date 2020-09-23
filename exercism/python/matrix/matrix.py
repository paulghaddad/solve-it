class Matrix:
    def __init__(self, matrix_string):
        self.matrix = Matrix.process_matrix_string(matrix_string)


    def row(self, index):
        return self.matrix[index-1]


    def column(self, index):
        return list([col for col in zip(*self.matrix)][index-1])


    def process_matrix_string(string):
        return [[int(el) for el in row.split()] for row in string.splitlines()]
