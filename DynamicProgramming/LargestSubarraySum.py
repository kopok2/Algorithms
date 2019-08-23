# coding=utf-8
"""Largest sum contiguous subarray dynamic programming solution Python implementation."""


def lscs(array):
    mx = 0
    mc = 0
    for x in array:
        mc = max(x + mc, 0)
        mx = max(mx, mc)
    return mx


if __name__ == "__main__":
    array = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(lscs(array))
