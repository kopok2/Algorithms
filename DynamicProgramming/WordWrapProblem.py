# coding=utf-8
"""Word wrap problem dynamic programming solution Python implementation."""


def wrap(text, limit):
    n = len(text)

    inf = sum(text) + 1
    ex = [[0 for x in range(n + 1)] for y in range(n + 1)]
    dp = [[0 for x in range(n + 1)] for y in range(n + 1)]
    c = [0 for x in range(n + 1)]
    p = [0 for x in range(n + 1)]
    for i in range(1, n + 1):
        ex[i][i] = limit - text[i - 1]
        for j in range(i + 1, n + 1):
            ex[i][j] = ex[i][j - 1] - text[j - 1] - 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if ex[i][j] < 0:
                dp[i][j] = inf
            elif j == n and ex[i][j] >= 0:
                dp[i][j] = 0
            else:
                dp[i][j] = ex[i][j] ** 2
    for j in range(1, n + 1):
        c[j] = inf
        for i in range(1, j + 1):
            if c[i - 1] != inf and dp[i][j] != inf and (c[i - 1] + dp[i][j] < c[j]):
                c[j] = c[i - 1] + dp[i][j]
                p[j] = i
    return p


if __name__ == "__main__":
    print(wrap([3, 2, 2, 5], 6))
