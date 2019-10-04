# coding=utf-8
"""Exponent calculation using Taylor series.

e^x = 1 + x/1! + x^2/2! + x^3/3! + ...
"""

import math


def exponent(n, x):
    ss = 1
    for i in range(n, 0, -1):
        ss = 1 + x * ss / i
    return ss


if __name__ == '__main__':
    for x in range(1, 101):
        print(x, exponent(x, 1), math.exp(1), exponent(x, 1) - math.exp(1))
