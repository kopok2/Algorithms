# coding=utf-8
"""Horner's method for polynomial evaluation in O(n) time Python implementation."""


def horner(poly, x):
    result = poly[0]
    for i in range(1, len(poly)):
        result = result * x + poly[i]
    return result


if __name__ == '__main__':
    poly = [2, -6, 2, -1]
    x = 3
    print(horner(poly, x))
