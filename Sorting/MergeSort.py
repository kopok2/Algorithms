"""Merge sort Python implementation."""


import math


def merge_sort(array):
    # sort bins
    for x in range(len(array) // 2):
        if array[x * 2] > array[x * 2 + 1]:
            swap = array[x * 2]
            array[x * 2] = array[x * 2 + 1]
            array[x * 2 + 1] = swap

    # merge bins
    merge_size = 4
    while True:
        for x in range(len(array) // merge_size + int(math.ceil(len(array) % merge_size / merge_size))):
            L = array[x * merge_size: x * merge_size + merge_size // 2]
            R = array[x * merge_size + merge_size // 2: x * merge_size + merge_size]
            k = x * merge_size
            i = 0
            j = 0
            while i < len(L) and j < len(R):
                if L[i] > R[j]:
                    array[k] = R[j]
                    j += 1
                else:
                    array[k] = L[i]
                    i += 1
                k += 1
            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                array[k] = R[j]
                j += 1
                k += 1

        if merge_size > len(array):
            break
        merge_size *= 2
