# coding=utf-8
"""Tiling problem dynamic programming solution Python implementation."""


def tiling(n):
    return n if n == 1 or n == 2 else tiling(n - 1) + tiling(n - 2)


if __name__ == "__main__":
    print(tiling(12))
    for x in range(1, 20):
        print(x, tiling(x))
