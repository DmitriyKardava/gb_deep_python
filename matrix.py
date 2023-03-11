from random import randint


class Matrix:
    def __init__(self, row, col):
        self.matrix = [[0 for _ in range(col)] for _ in range(row)]

    def fill_random(self):
        self.matrix = [[randint(0, 10) for _ in range(len(self.matrix))] for _ in range(len(self.matrix[0]))]

    def _is_equal(self, other):
        if len(self.matrix) == len(other.matrix) or len(self.matrix[0]) == len(other.matrix[0]):
            return True
        else:
            return False

    def __str__(self):
        return '\n'+'\n'.join(['\t'.join(map(str, lst)) for lst in self.matrix])+'\n'

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if not self._is_equal(other):
            raise ValueError
        result = Matrix(len(self.matrix), len(self.matrix[0]))
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result.matrix[i][j] = other.matrix[i][j] + self.matrix[i][j]
        return result

    def __sub__(self, other):
        if not self._is_equal(other):
            raise ValueError
        result = Matrix(len(self.matrix), len(self.matrix[0]))
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result.matrix[i][j] = other.matrix[i][j] - self.matrix[i][j]
        return result

    def __eq__(self, other):
        return True if self.matrix == other.matrix else False

    def __gt__(self, other):
        return True if self.matrix > other.matrix else False

    def __ge__(self, other):
        return True if self.matrix >= other.matrix else False

    def __lt__(self, other):
        return True if self.matrix < other.matrix else False

    def __le__(self, other):
        return True if self.matrix <= other.matrix else False


if __name__ == "__main__":
    m1 = Matrix(3, 4)
    m1.fill_random()
    m2 = Matrix(3, 4)
    m2.fill_random()
    print(f"{m1 =}")
    print(f"{m2 =}")
    print(f"{m1 + m2 =}")
