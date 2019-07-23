"""Quick sort Python implementation."""


def partition(array, l, h):
    i = l - 1
    x = array[h]
    for j in range(l, h):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[h] = array[h], array[i + 1]
    return i + 1


def quick_sort(array):
    l = 0
    h = len(array) - 1
    to_part = [(l, h)]
    while to_part:
        parting = to_part.pop(0)
        l = parting[0]
        h = parting[1]
        mid = partition(array, *parting)
        if mid > l:
            to_part.append((l, mid - 1))
        if mid < h:
            to_part.append((mid, h))
