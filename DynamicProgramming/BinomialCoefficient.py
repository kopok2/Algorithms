# coding=utf-8
"""Binomial coefficient calculation using dynamic programming Python implementation."""


def binomial_coefficient(n, k):
    dp = [0 for x in range(k + 1)]
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            dp[j] = dp[j] + dp[j - 1]
    return dp[k]


if __name__ == "__main__":
    print(binomial_coefficient(5, 2))
