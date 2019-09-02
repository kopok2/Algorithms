# coding=utf-8
"""Optimal printing problem dynamic programming solution Python implementation."""


def opp(n):
    if n <= 6:
        return n
    dp = [0] * n
    b = 0
    for i in range(1, 7):
        dp[i - 1] = i
    for i in range(7, n + 1):
        for b in range(i - 3, 0, -1):
            curr = (i - b - 1) * dp[b - 1]
            if curr > dp[i - 1]:
                dp[i - 1] = curr
    return dp[n - 1]


if __name__ == "__main__":
    for x in range(1, 21):
        print(x, opp(x))
