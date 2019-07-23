"""Insertion sort Python implementation."""


def insertion_sort(array):
    for x in range(1, len(array)):
        y = x
        while array[y] < array[y - 1]:
            swap = array[y]
            array[y] = array[y - 1]
            array[y - 1] = swap
            y -= 1
            if not y:
                break
