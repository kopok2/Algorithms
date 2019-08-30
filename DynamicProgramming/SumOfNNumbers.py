# coding=utf-8
"""Sum of numbers from 1 to N dymamic programming solution Python implementation."""

import math


def util(n, a):
    if n < 10:
        return n * (n - 1) // 2
    d = int(math.log10(n))
    p = int(math.ceil(math.pow(10, d)))
    msd = n / p
    return msd * a[d] + (msd * (msd - 1) / 2) * p + msd * (1 + n % p) + util(n % p, a)


def sodf1tn(n):
    d = int(math.log10(n))
    a = [0] * (d + 1)
    a[0] = 0
    a[1] = 45
    for i in range(2, d + 1):
        a[i] = a[i - 1] * 10 + 45 * int(math.ceil(math.pow(10, i - 1)))
    return util(n, a)


if __name__ == "__main__":
    print(sodf1tn(328))
