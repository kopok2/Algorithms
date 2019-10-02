# coding=utf-8
"""Space and time efficient Binomial Coefficient algorithm."""


def bin_coef(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res


if __name__ == '__main__':
    print(bin_coef(8, 2))
