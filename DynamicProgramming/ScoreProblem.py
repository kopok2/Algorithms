# coding=utf-8
"""Score problem dynamic programming solution Python implementation."""


def sp(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(3, n + 1):
        dp[i] += dp[i - 3]
    for i in range(5, n + 1):
        dp[i] += dp[i - 5]
    for i in range(10, n + 1):
        dp[i] += dp[i - 10]
    return dp[n]


if __name__ == "__main__":
    for x in range(101):
        print(x, sp(x))
