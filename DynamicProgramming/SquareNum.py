# coding=utf-8
"""Minimal square sum number problem dynamic programming solution Python implementation."""

import math


def mssn(n):
    dp = [x for x in range(n + 1)]
    for x in range(1, int(math.ceil(math.sqrt(n)))+ 1):
        tmp = x ** 2
        if tmp > n:
            break
        else:
            dp[n] = min(dp[n], 1 + dp[n - tmp])
    return dp[n]


if __name__ == "__main__":
    print(mssn(100))
    for x in range(1, 1001):
        print(x, mssn(x))
