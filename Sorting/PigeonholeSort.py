# coding=utf-8
"""Pigeonhole sort Python implementation."""


def pigeonhole_sort(array):
    arr_min = min(array)
    size = max(array) - arr_min + 1
    holes = [0 for x in range(size)]

    for x in array:
        holes[x - arr_min] += 1

    i = 0
    for count in range(size):
        while holes[count]:
            holes[count] -= 1
            array[i] = count + arr_min
            i += 1
