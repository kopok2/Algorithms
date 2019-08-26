# coding=utf-8
"""Stairs problem dynamic programming solution Python implementation."""


def stairs(n, m):
    n = n + 1
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        dp[i] = 0
        j = 1
        while j <= m and j <= i:
            dp[i] += dp[i - j]
            j += 1
    return dp[n - 1]


if __name__ == "__main__":
    print(stairs(4, 2))
