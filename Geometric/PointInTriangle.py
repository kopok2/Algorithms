# coding=utf-8
"""Point in triangle."""


def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) / 2))


def in_triangle(x1, y1, x2, y2, x3, y3, x, y):
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)
    print(A - (A1 + A2 + A3))
    return A - (A1 + A2 + A3) < 0.001


if __name__ == "__main__":
    print(in_triangle(0, 0, 20, 0, 10, 30, 10, 12))
