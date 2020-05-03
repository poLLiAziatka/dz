import random


class Matrix:
    def __init__(self, data=None, shape=None):
        self.data = data
        self.shape = shape
        if self.data is None:
            self.data = []
            for i in range(int(shape[0])):
                self.data.append([random.randint(-100, 100) for x in range(int(shape[1]))])
        elif not self.shape:
            self.shape = (len(self.data), len(self.data[0]))

    def check_shape_for_add(self, matrix):
        if self.shape == matrix.shape:
            return True
        return False

    def check_shape_for_mul(self, matrix):
        if self.shape[0] == matrix.shape[0] or self.shape[0] == matrix.shape[1] or self.shape[1] == matrix.shape[0] or \
                self.shape[1] == matrix.shape[1]:
            return True
        return False

    def check_shape_square(self):
        if self.shape[0] == self.shape[1]:
            return True
        return False

    def __add__(self, other):
        if self.check_shape_for_add(other):
            new_matrix = Matrix(shape=self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix[i][j] = self.data[i][j] + other.data[i][j]
        return new_matrix

    def __iadd__(self, other):
        if self.check_shape_for_add(other):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.data[i][j] += other.data[i][j]
            return self

    def __sub__(self, other):
        if self.check_shape_for_add(other):
            new_matrix = Matrix(shape=self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix[i][j] = self.data[i][j] - other.data[i][j]
            return new_matrix

    def __isub__(self, other):
        if self.check_shape_for_add(other):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.data[i][j] -= other.data[i][j]
            return self

    def __mul__(self, other):
        if type(other) == list:
            if self.check_shape_for_mul(other):
                new_matrix = Matrix(shape=self.shape)
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        for k in range(other.shape[0]):
                            new_matrix.data[i * self.shape[1]][j] = self.data[i * other.other.shape[0] + k] * \
                                                                    other.data[k * self.shape[1] + j]
                return new_matrix

        if type(other) == int or type(other) == float:

            new_matrix = Matrix(data=self.data)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix.data[i][j] *= other
            return new_matrix

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f'Matrix(data={self.data}, shape={self.shape})'

    def __setitem__(self, key_m, key_n, value):
        self.data[key_m][key_n] = value

    def __getitem__(self, key_m):
        return self.data[key_m]

    def determinant(self, matrix=None, mul=1):
        if matrix is None:
            matrix = self.data
            if not self.check_shape_square():
                return None
        width = len(matrix)
        if width == 1:
            return mul * matrix[0][0]
        else:
            sign = -1
            det = 0
            for i in range(width):
                m = []
                for j in range(1, width):
                    buff = []
                    for k in range(width):
                        if k != i:
                            buff.append(matrix[j][k])
                    m.append(buff)
                sign *= -1
                det += mul * self.determinant(m, sign * matrix[0][i])
            return det

    def is_degenerate(self):
        return self.determinant() == 0

    def kramer_solution(self, b):
        x = []
        data_matrix = self.data.copy()
        matrix = Matrix(data=data_matrix)
        det = matrix.determinant()
        for i in range(matrix.shape[1]):
            matrix = Matrix(data=self.data.copy())
            matrix.data[:] = [list(x) for x in list(zip(*matrix.data))]
            matrix.data[i] = b
            matrix.data[:] = [list(x) for x in list(zip(*matrix.data))]
            det_i = matrix.determinant()
            x.append(det_i / det)
        return x

    def gauss_solution(self, b):

        matrix = Matrix(data=self.data.copy())
        matrix.data[:] = [list(x) for x in list(zip(*matrix.data))]
        matrix.data.append(b)
        matrix.data[:] = [list(x) for x in list(zip(*matrix.data))]

        for i in range(matrix.shape[1]):
            for j in range(i + 1, matrix.shape[0]):
                r = [(x * (-(matrix.data[j][i] / matrix.data[i][i]))) for x in matrix.data[i]]
                matrix.data[j] = [sum(pair) for pair in zip(matrix.data[j], r)]

        x = []
        matrix.data.reverse()
        for sol in range(matrix.shape[0]):
            if sol == 0:
                x.append(matrix.data[sol][-1] / matrix.data[sol][-2])
            else:
                n = 0
                for i in range(sol):
                    n += (x[i] * matrix.data[sol][-2 - i])
                x.append((matrix.data[sol][-1] - n) / matrix.data[sol][-sol - 2])
        x.reverse()
        return x

    def inverse(self):
        def some_func(m, x):
            matrix = Matrix(data=m.data.copy())
            n = matrix.shape[0]
            row = max(range(x, n), key=lambda i: abs(matrix.data[i][x]))
            if x != row:
                matrix.data[x], matrix.data[row] = matrix.data[row], matrix.data[x]
            return matrix

        matrix = Matrix(data=self.data.copy())
        n = matrix.shape[0]

        for i in range(n):
            matrix.data[i] += [int(i == j) for j in range(n)]

        for x in range(n):
            matrix = some_func(matrix, x)
            for i in range(x + 1, n):
                coef = matrix.data[i][x] / matrix.data[x][x]
                for j in range(x, n * 2):
                    matrix.data[i][j] -= coef * matrix.data[x][j]

        for x in reversed(range(n)):
            for i in reversed(range(x)):
                coef = matrix.data[i][x] / matrix.data[x][x]
                for j in reversed(range(n * 2)):
                    matrix.data[i][j] -= coef * matrix.data[x][j]

        for i in range(n):
            a = matrix.data[i][i]
            for j in range(n*2):
                matrix.data[i][j] /= a


        return [matrix.data[i][n:] for i in range(n)]






