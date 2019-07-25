"""Radix sort Python implementation."""


def counting_sort_radix(array, digit):
    dig_arr = [x % (10 ** digit) for x in array]
    ol_arr = array.copy()
    counts = [dig_arr.count(y) for y in range(10 ** digit)]
    for x in range(len(counts) - 1):
        counts[x + 1] += counts[x]
    for x in range(len(array)):
        array[counts[ol_arr[x]% (10 ** digit)]  - 1] = ol_arr[x]
        counts[ol_arr[x]% (10 ** digit)] -= 1


def radix_sort(array):
    for d in range(1, max([len(str(x)) for x in array]) + 1):
        counting_sort_radix(array, d)
