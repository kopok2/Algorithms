# coding=utf-8
"""Babylonian Square Root."""

import math


def sqrt(x, e=0.000000000001):
    """Babylonian Square Root algorithm.

    Args:
        x: number to take square root of.
        e: precision.

    Returns:
        square root of x with precision e.
    """
    n = x
    y = 1
    while n - y > e and n:
        n = (n + y) / 2
        y = x / n
    return n


if __name__ == '__main__':
    # compare math.sqrt results with Babylonian Square Root results.
    for x in range(1000):
        print(x, math.sqrt(x), sqrt(x), math.sqrt(x) - sqrt(x))
