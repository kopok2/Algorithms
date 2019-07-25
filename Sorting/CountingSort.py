"""Counting sort Python implementation."""


def counting_sort(array):
    counts = [0 for x in range(max(array) + 1)]
    for x in array:
        counts[x] += 1
    x = 0
    adding = 0
    while x < len(array):

        for y in range(counts[adding]):
            array[x] = adding
            x += 1
        adding += 1
