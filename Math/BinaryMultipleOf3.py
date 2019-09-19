# coding=utf-8
"""Binary solution to check whether given number is a multiple of 3."""


def is_mult(n):
    oc = 0
    ec = 0
    n = abs(n)
    if not n:
        return True
    if n == 1:
        return False
    while n:
        if n & 1:
            oc += 1
        if n & 2:
            ec += 1
        n >>= 2
    return is_mult(abs(oc - ec))


if __name__ == "__main__":
    print(24, is_mult(24))
    print(7, is_mult(7))
    for x in range(101):
        print(x, is_mult(x), x % 3)
