# coding=utf-8
"""Points intersection algorithm Python implementation."""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def on_segment(p, q, r):
    return max(p.x, r.x) >= q.x >= min(p.x, r.x) and max(p.y, r.y) >= q.y >= min(p.y, r.y)


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if not val:
        return 0
    else:
        return 1 if val > 0 else 2


def do_intersect(p1, q1, p2, q2):
    o1, o2, o3, o4 = orientation(p1, q1, p2), orientation(p1, q1, q2), orientation(p2, q2, p1), orientation(p2, q2, q1)
    if o1 != o2 and o3 != o4:
        return True
    if not o1 and on_segment(p1, p2, q1):
        return True
    if not o2 and on_segment(p1, q2, q1):
        return True
    if not o3 and on_segment(p2, p1, q2):
        return True
    if not o4 and on_segment(p2, q1, q2):
        return True
    return False


if __name__ == "__main__":
    p1 = Point(1, 1)
    q1 = Point(10, 1)
    p2 = Point(1, 2)
    q2 = Point(10, 2)
    print(do_intersect(p1, q1, p2, q2))

    p1 = Point(10, 0)
    q1 = Point(0, 10)
    p2 = Point(0, 0)
    q2 = Point(10, 10)
    print(do_intersect(p1, q1, p2, q2))

    p1 = Point(-5, -5)
    q1 = Point(0, 0)
    p2 = Point(1, 1)
    q2 = Point(10, 10)
    print(do_intersect(p1, q1, p2, q2))
