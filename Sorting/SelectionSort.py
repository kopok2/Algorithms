"""Selection sort Python implementation."""


def selection_sort(array):
    for x in range(len(array)):
        min = array[x]
        id = x
        for y in range(x + 1, len(array)):
            if array[y] < min:
                id = y
                min = array[y]
        swap = array[x]
        array[x] = array[id]
        array[id] = swap
