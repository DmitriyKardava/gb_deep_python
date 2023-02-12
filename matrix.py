"""
Напишите функцию для транспонирования матрицы
"""


def transposition(matrix: []):
    result = [[None for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[j][i] = matrix[i][j]
    return result


m = [[1, 2, 3],
     [4, 5, 6]]
print(transposition(m))
