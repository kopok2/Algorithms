# coding=utf-8
"""Number Point Composition math algorithm."""

import math

ARR = [0] * 100
CNT = 0

def p_compose(n, i):

    if not n:
        global CNT
        CNT += 1
        print(ARR[:i])
    elif n > 0:
        for k in range(1, n + 1):
            ARR[i] = k
            p_compose(n - k, i + 1)


if __name__ == '__main__':
    p_compose(20, 0)
    print(CNT)
