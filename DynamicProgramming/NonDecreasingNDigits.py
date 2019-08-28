# coding=utf-8
"""Non decreasing n-digits dynamic programming solution Python implementation."""


def ndnd(n):
    dp = [[0] * 10 for x in range(n + 1)]
    for i in range(10):
        dp[i][1] = 1
    for digit in range