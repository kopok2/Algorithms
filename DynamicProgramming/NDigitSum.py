# coding=utf-8
"""N-Digit sum problem dynamic programming solution Python implementation."""

import math


def nds(n, ss):
    start = math.pow(10, n - 1)
    stop = math.pow(10, n) - 1
    cnt = 0
    i = start
    while i <= stop:
        cur = 0
        tmp = i
        while tmp:
            cur += tmp % 10
            tmp //= 10
        if cur == ss:
            cnt += 1
            i += 9
        else:
            i += 1
    return cnt


if __name__ == "__main__":
    print(nds(3, 5))
