# coding=utf-8


def count(n):
    if n < 3:
        return n
    if n >= 3 and n < 10:
        return n - 1
    po = 1
    while n / po > 9:
        po *= 10
    msd = n // po
    if msd != 3:
        return count(msd) * count(po - 1) + count(msd) + count(n % po)
    else:
        return count(msd * po - 1)


if __name__ == '__main__':
    print(count(54))
