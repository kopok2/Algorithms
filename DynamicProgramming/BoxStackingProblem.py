# coding=utf-8
"""Box stacking problem dynamic programming solution Python implementation."""


class Box:
    def __init__(self, w=0, d=0, h=0):
        self.w = w
        self.d = d
        self.h = h

    def __lt__(self, other):
        return self.d * self.w < other.d * other.w


def stack_height(boxes):
    n = len(boxes)
    rotated = [Box() for x in range(3 * n)]
    index = 0
    for i in range(n):
        rotated[index].h = boxes[i].h
        rotated[index].d = max(boxes[i].d, boxes[i].w)
        rotated[index].w = min(boxes[i].d, boxes[i].w)
        index += 1
        rotated[index].h = boxes[i].w
        rotated[index].d = max(boxes[i].h, boxes[i].d)
        rotated[index].w = min(boxes[i].h, boxes[i].d)
        index += 1
        rotated[index].h = boxes[i].d
        rotated[index].d = max(boxes[i].h, boxes[i].w)
        rotated[index].w = min(boxes[i].h, boxes[i].w)
        index += 1
    n *= 3
    rotated.sort(reverse=True)
    dp = [rotated[i].h for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if rotated[i].w < rotated[j].w and rotated[i].d < rotated[j].d:
                dp[i] = max(dp[i], dp[j] + rotated[i].h)
    return max(dp)


if __name__ == "__main__":
    array = [Box(4, 6, 7), Box(1, 2, 3), Box(4, 5, 6), Box(10, 12, 32)]
    print(stack_height(array))
