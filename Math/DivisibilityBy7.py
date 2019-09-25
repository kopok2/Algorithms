# coding=utf-8
"""Divisibility by 7 without modulo operator."""


def div_by_7(n):
    if n < 0:
        return div_by_7(- n)
    if not n or n == 7:
        return True
    elif n < 10:
        return False
    return div_by_7(n // 10 - 2 * (n - n // 10 * 10))


if __name__ == '__main__':
    for x in range(100):
        print(x, div_by_7(x))
