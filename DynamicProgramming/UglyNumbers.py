# coding=utf-8
"""Numbers with only prime factors = 2, 3 or 5. Dynamic programming solution Python implementation."""


def un(n):
    ugly = [0] * n
    ugly[0] = 1
    i2 = i3 = i5 = 0
    nm2 = 2
    nm3 = 3
    nm5 = 5
    nno = 1
    for i in range(1, n):
        nno = min(nm2, nm3, nm5)
        ugly[i] = nno
        if nno == nm2:
            i2 += 1
            nm2 = ugly[i2] * 2
        elif nno == nm3:
            i3 += 1
            nm3 = ugly[i3] * 3
        elif nno == nm5:
            i5 += 1
            nm5 = ugly[i5] * 5
    print(ugly)
    return nno


if __name__ == "__main__":
    print(un(150))
