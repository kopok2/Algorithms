# coding=utf-8
"""Cutting rod problem dynamic programming solution Python implementation."""


def ctr(n, prices):
    dp = [0 for x in range(n + 1)]
    for i in range(1, n + 1):
        mx = 0
        for j in range(i):
            mx = max(mx, prices[j] + dp[i - j - 1])
        dp[i] = mx
    return dp[n]


if __name__ == "__main__":
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    print(ctr(8, arr))
