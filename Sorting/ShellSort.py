# coding=utf-8
"""Shell sort Python implementation."""


def shell_sort(array):
    g = len(array) // 2
    while g > 0:
        for i in range(g, len(array)):
            temp = array[i]
            j = i
            while j >= g and array[j - g] > temp:
                array[j] = array[j - g]
                j -= g
            array[j] = temp
        g //= 2
