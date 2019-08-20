# coding=utf-8
"""Maximum binary on submatrix dynamic programming solution Python implementation."""


def mxbos(matrix):
    dp = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if not x or not y:
                dp[y][x] = matrix[y][x]
            elif matrix[y][x]:
                dp[y][x] = min(dp[y - 1][x], dp[y - 1][x - 1], dp[y][x - 1]) + 1
            else:
                dp[y][x] = 0
    return max([max(row) for row in dp])


if __name__ == "__main__":
    matrix = [[0, 1, 1, 0, 1],
              [1, 1, 0, 1, 0],
              [0, 1, 1, 1, 0],
              [1, 1, 1, 1, 0],
              [1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0]]
    print(mxbos(matrix))
