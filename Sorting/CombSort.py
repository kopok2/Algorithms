# coding=utf-8
"""Comb sort Python implementation."""


def comb_sort(array):
    gap = len(array)
    swapped = True
    while gap != 1 or swapped:
        gap = gap * 10 / 13
        if gap < 1:
            gap = 1
        gap = int(gap)
        swapped = False
        for i in range(len(array) - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True
