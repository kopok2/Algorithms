# coding=utf-8
"""Square validation."""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist_sq(p, q):
    return  (p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y)


def valid_square(p1, p2, p3, p4):
    d2 = dist_sq(p1, p2)
    d3 = dist_sq(p1, p3)
    d4 = dist_sq(p1, p4)
    if d2 == d3 and 2 * d2 == d4 and 2 * dist_sq(p2, p4) == dist_sq(p2, p3):
        return True
    if d3 == d4 and 2 * d3 == d2 and 2 * dist_sq(p3, p2) == dist_sq(p3, p4):
        return True
    if d2 == d4 and 2 * d2 == d3 and 2 * dist_sq(p2, p3) == dist_sq(p2, p4):
        return True
    return False


if __name__ == '__main__':
    print(valid_square(*[Point(*x) for x in [(20, 10), (10, 20), (20, 20), (10, 10)]]))
