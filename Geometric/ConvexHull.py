# coding=utf-8
"""Convex Hull Geometric Algorithm solution Python implementation."""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point: x:{0} y:{1}".format(self.x, self.y)


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if not val:
        return 0
    else:
        return 1 if val > 0 else 2


def convex_hull(points):
    n = len(points)
    hull = []
    l = 0
    for i in range(1, n):
        if points[i].x < points[l].x:
            l = i
    p = l
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == l:
            break
    return hull


if __name__ == "__main__":
    points = [Point(*x) for x in [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]]
    print(convex_hull(points))
