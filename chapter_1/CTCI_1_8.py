"""Zero Matrix: write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

ex:

input: [[1, 2, 3],
        [4, 5, 0],
        [4, 5, 6]]

ouput: [[1, 2, 0],
        [0, 0, 0],
        [4, 5, 0]]"""


def zero_matrix(input_matrix):
    """."""
    rows = len(input_matrix)
    cols = len(input_matrix[0])
    zeros = []

    for i in range(rows):
        for j in range(cols):
            if input_matrix[i][j] == 0:
                zeros.append((i, j))

    for zero in zeros:
        for i in range(rows):
            input_matrix[i][zero[1]] = 0

        for j in range(cols):
            input_matrix[zero[0]][j] = 0

    return input_matrix
