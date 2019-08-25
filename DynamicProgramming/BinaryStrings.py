# coding=utf-8
"""Binary strings without consecutive 1's dynamic programming solution Python implementation."""


def bswc1(n):
    dpa = [1] * n
    dpb = [1] * n
    for i in range(1, n):
        dpa[i] = dpa[i - 1] + dpb[i - 1]
        dpb[i] = dpa[i - 1]
    return dpa[n - 1] + dpb[n - 1]


if __name__ == "__main__":
    print(bswc1(3))
    for x in range(1, 100):
        print(x, bswc1(x))
