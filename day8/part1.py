data = open('input.txt').read().splitlines()

tree_matrix = [list(row) for row in data]


def visible_from_left(matrix, i, j):
    return all([matrix[i][j] > x for x in matrix[i][:j]])


def visible_from_right(matrix, i, j):
    return all([matrix[i][j] > x for x in matrix[i][j + 1:]])


def visible_from_top(matrix, i, j):
    above = [matrix[z][j] for z in range(i)]
    return all([matrix[i][j] > x for x in above])


def visible_from_bottom(matrix, i, j):
    below = [matrix[z][j] for z in range(i + 1, len(matrix))]
    return all([matrix[i][j] > x for x in below])


tree_count = len(data) * 4 - 4
for i in range(1, len(tree_matrix) - 1):
    for j in range(1, len(tree_matrix[0]) - 1):
        if visible_from_left(tree_matrix, i, j) or visible_from_right(tree_matrix, i, j) or visible_from_top(
                tree_matrix, i, j) or visible_from_bottom(tree_matrix, i, j):
            tree_count += 1

print(tree_count)
