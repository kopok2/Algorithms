# coding=utf-8
"""Point in Polygon problem solution Python implementation."""


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


def is_inside(polygon, p):
    n = len(polygon)
    if n < 3:
        return False
    extreme = Point(10000, p.y)
    cnt, i = 0, 0
    while True:
        nxt = (i + 1) % n
        if do_intersect(polygon[i], polygon[nxt], p, extreme):
            if not orientation(polygon[i], p, polygon[nxt]):
                return on_segment(polygon[i], p, polygon[nxt])
            cnt += 1
        i = nxt
        if not i:
            break
    return cnt % 2 == 1


if __name__ == "__main__":
    polygon1 = [Point(*x) for x in [(0, 0), (10, 0), (10, 10), (0, 10)]]
    p = Point(20, 20)
    print(is_inside(polygon1, p))
    p = Point(5, 5)
    print(is_inside(polygon1, p))

    polygon2 = [Point(*x) for x in [(0, 0), (5, 5), (5, 0)]]
    p = Point(3, 3)
    print(is_inside(polygon2, p))
    p = Point(5, 1)
    print(is_inside(polygon2, p))
    p = Point(8, 1)
    print(is_inside(polygon2, p))

    polygon3 = [Point(*x) for x in [(0, 0), (10, 0), (10, 10), (0, 10)]]
    p = Point(-1, 10)
    print(is_inside(polygon3, p))
