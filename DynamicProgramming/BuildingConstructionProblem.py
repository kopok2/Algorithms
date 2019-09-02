# coding=utf-8
"""Building construction problem dynamic programming solution Python implementation."""


def bcp(n):
    n += 2
    w = [0] * (n + 2)
    w[0] = 0
    w[1] = 1
    for i in range(2, n + 1):
        w[i] = w[i - 1] + w[i - 2]
    return w[n] ** 2


if __name__ == "__main__":
    for x in range(1, 101):
        print(x, bcp(x))
