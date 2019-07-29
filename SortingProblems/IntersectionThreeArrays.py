# encoding-utf-8
"""Find intersection of three sorted arrays."""


def intersect(a1, a2):
    t1 = a1.copy()
    t2 = a2.copy()
    t1.sort()
    t2.sort()
    print(t1, t2)
    result = []
    while t1 and t2:
        if t1[-1] == t2[-1]:
            result.append(t1.pop())
            t2.pop()
        elif t1[-1] > t2[-1]:
            t1.pop()
        else:
            t2.pop()
    return result


def intersect_of_three(a1, a2, a3):
    return intersect(intersect(a1, a2), a3)


if __name__ == "__main__":
    a1 = [1, 2, 3, 4, 5, 6]
    a2 = [3, 4, 5, 6, 7, 8]
    print(intersect(a1, a2))
    a3 = [4, 3, 0, 12]
    print(intersect_of_three(a1, a2, a3))
