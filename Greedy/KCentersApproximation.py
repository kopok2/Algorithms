# coding=utf-8
"""K-Center approximate algorithm Python implementation."""


def k_centers(points, k):
    centers = [0]
    k -= 1
    while k:
        remains = []
        for x in range(len(points)):
            if x not in centers:
                remains.append((x, min([points[x][y] for y in range(len(points[x])) if y in centers])))
        remains.sort(key=lambda z: z[1], reverse=True)
        centers.append(remains[0][0])
        k -= 1
    return centers


if __name__ == "__main__":
    points = [[0, 1, 1, 2, 3], [1, 0, 2, 1, 2], [1, 2, 0, 1, 3], [2, 1, 1, 0, 2], [3, 2, 3, 2, 0]]
    print(k_centers(points, 2))
