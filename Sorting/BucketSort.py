# coding=utf-8
"""Bucket sort Python implementation."""

from InsertionSort import insertion_sort


def bucket_sort(array):
    try:
        min_a = min(array)
        max_a = max(array)
        len_a = len(array)
        buckets = [[] for x in range(len_a + 10)]
        for x in array:
            buckets[int(len_a * x / (max_a - min_a))].append(x)
        for b in buckets:
            insertion_sort(b)
        narray = []
        for b in buckets:
            narray += b
        for x in range(len_a):
            array[x] = narray[x]
    except ZeroDivisionError:
        pass

