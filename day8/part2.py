import numpy as np

data = open('input.txt').read().splitlines()

tree_matrix = [list(row) for row in data]


def score_left(matrix, i, j):
    bigguns = [z for z in range(j) if matrix[i][j] <= matrix[i][z]]
    if not bigguns:
        return j
    return j - np.max(bigguns)


def score_right(matrix, i, j):
    bigguns = [z for z in range(j + 1, len(matrix[0])) if matrix[i][j] <= matrix[i][z]]
    if not bigguns:
        return len(matrix[0]) - 1 - j
    return np.min(bigguns) - j


def score_top(matrix, i, j):
    above = [matrix[z][j] for z in range(i)]
    bigguns = [z for z in range(len(above)) if matrix[i][j] <= above[z]]
    if not bigguns:
        return i
    return i - np.max(bigguns)


def score_bottom(matrix, i, j):
    below = [matrix[z][j] for z in range(i + 1, len(matrix))]
    bigguns = [z for z in range(len(below)) if matrix[i][j] <= below[z]]
    if not bigguns:
        return len(matrix) - 1 - i
    return np.min(bigguns) + 1


def scenic_score(matrix, i, j):
    return score_left(matrix, i, j) * score_right(matrix, i, j) * score_top(matrix, i, j) * score_bottom(matrix, i, j)


maxi = 0
for i in range(1, len(tree_matrix) - 1):
    for j in range(1, len(tree_matrix[0]) - 1):
        score = scenic_score(tree_matrix, i, j)
        if maxi < score:
            maxi = score

print(maxi)
