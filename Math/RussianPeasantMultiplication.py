# coding=utf-8
"""Russian Peasant Multiplication algorithm Python implementation."""


def russ_peasant(a, b):
    res = 0
    while b > 0:
        if b & 1:
            res += a
        a <<= 1
        b >>= 1
    return res


if __name__ == '__main__':
    for x in range(10):
        for y in range(10):
            print(x, y, x * y, russ_peasant(x, y))
