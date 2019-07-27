# coding=utf-8
"""Cycle sort Python implementation."""


def cycle_sort(array):
    for c in range(len(array) - 1):
        item = array[c]
        pos = c
        i = c + 1
        while i < len(array):
            if array[i] < item:
                pos += 1
            i += 1
        if pos != c:
            while item == array[pos]:
                pos += 1
            item, array[pos] = array[pos], item
            while pos != c:
                pos = c
                i = c + 1
                while i < len(array):
                    if array[i] < item:
                        pos += 1
                    i += 1
                while item == array[pos]:
                    pos += 1
                if item != array[pos]:
                    item, array[pos] = array[pos], item
