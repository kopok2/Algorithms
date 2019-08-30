# coding=utf-8
"""Shortest Common Supersequence problem dynamic programming solution Python implementation."""


def ss(x, y):
    m = len(x)
    n = len(y)
    dp = [[0 for x in range(n + 1)] for y in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if not i:
                dp[i][j] = j
            elif not j:
                dp[i][j] = i
            elif x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


if __name__ == "__main__":
    print(ss("AGGTAB", "GXTXAYB"))
