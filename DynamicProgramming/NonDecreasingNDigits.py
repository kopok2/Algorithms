# coding=utf-8
"""Non decreasing n-digits dynamic programming solution Python implementation."""


def ndnd(n):
    dp = [[0] * 10 for x in range(n + 1)]
    for i in range(10):
        dp[1][i] = 1
    for digit in range(10):
        for l in range(2, n + 1):
            for x in range(digit + 1):
                dp[l][digit] += dp[l - 1][x]
    cnt = 0
    for i in range(10):
        cnt += dp[n][i]
    return cnt


if __name__ == "__main__":
    print(ndnd(3))
