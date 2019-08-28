# coding=utf-8
"""Minimum initial points dynamic progragmming solution Python implementation."""


def mip(way):
    r = len(way)
    c = len(way[0])
    dp = [[0 for x in range(c)] for y in range(r)]
    m = r
    n = c
    dp[m - 1][n - 1] = 1 if way[m - 1][n - 1] > 0 else abs(way[m - 1][n - 1]) + 1
    for i in range(m - 2, -1, -1):
        dp[i][n - 1] = max(dp[i + 1][n - 1] - way[i][n - 1], 1)
    for j in range(n - 2, -1, -1):
        dp[m - 1][j] = max(dp[m - 1][j + 1] - way[m - 1][j], 1)
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            mex = min(dp[i + 1][j], dp[i][j + 1])
            dp[i][j] = max(mex - way[i][j], 1)
    return dp[0][0]


if __name__ == "__main__":
    way = [[-2, -3, 3],
           [-5, -10, 1],
           [10, 30, -5]]
    print(mip(way))
