# encoding-utf-8
"""Find closest pair to number from to sorted arrays."""

def closest_pair(array1, array2, target):
    x = 0
    y = len(array2) - 1
    while x != y:
        if array1[x] + array2[y] == target:
            break
        elif array1[x] + array2[y] > target:
            y -= 1
        else:
            x += 1
    return array1[x], array2[y]


if __name__ == "__main__":
    a1 = [1, 2, 3, 4]
    a2 = [1, 2, 3, 4]
    print(closest_pair(a1, a2, 6))
