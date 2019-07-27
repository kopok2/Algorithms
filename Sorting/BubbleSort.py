# coding=utf-8
"""BubbleSort Python implementation."""


def bubble_sort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                swapped = True
                swap = array[j]
                array[j] = array[j + 1]
                array[j + 1] = swap
        if not swapped:
            break
