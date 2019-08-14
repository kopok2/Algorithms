# coding=utf-8
"""Given matrix of cost traverse to lower rights corner at mininmal cost."""


def min_cost(matrix):
    cost = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if not x and not y:
                cost[x][y] = matrix[x][y]
            elif not x:
                cost[x][y] = matrix[x][y - 1] + matrix[x][y]
            elif not y:
                cost[x][y] = matrix[x - 1][y] + matrix[x][y]
            else:
                cost[x][y] = min(cost[x - 1][y], cost[x][y - 1], cost[x - 1][y - 1]) + matrix[x][y]
    for c in cost:
        print(c)
    return cost[len(matrix) - 1][len(matrix[0]) - 1]


if __name__ == "__main__":
    matr = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
    for m in matr:
        print(m)
    print(min_cost(matr))
