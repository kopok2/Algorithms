# coding=utf-8
"""Fibonacci Number Check algorithm."""

import math


def is_perfect_square(n):
    s = int(math.sqrt(n))
    return s ** 2 == n


def is_fib(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


if __name__ == '__main__':
    for x in range(100):
        print(x, is_fib(x))
