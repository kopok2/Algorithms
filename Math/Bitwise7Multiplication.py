# coding=utf-8
"""Bitwise multiplication by 7."""


def mult_by_seven(n):
    return ((n << 3) - n)


if __name__ == '__main__':
    for x in range(10001):
        print(x, mult_by_seven(x), x * 7, x * 7 == mult_by_seven(x))
