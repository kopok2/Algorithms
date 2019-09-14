# coding=utf-8
"""Power of number Divide and Conquer algorithm solution Python implementation."""


def power(x, y):
    if not y:
        return 1
    t = power(x, y // 2)
    if not y % 2:
        return t * t
    else:
        if y > 0:
            return x * t * t
        else:
            return (t * t) / x


if __name__ == "__main__":
    for x in range(11):
        for y in range(11):
            print(power(x, y), x, y)
