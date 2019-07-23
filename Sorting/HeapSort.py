"""Heap sort Python implementation."""


def heap_sort(array):
    i = 1
    s = 1
    l = 0
    while s < len(array):
        i *= 2
        l += 1
        s += i
    start_i = i
    start_l = l
    start_s = s
    including_range = len(array)
    while including_range > 1:
        i = start_i
        l = start_l
        s = start_s
        while l:
            for x in range(i // 2):
                root = s - i - i // 2 + x
                left_child = s - i + x * 2
                right_child = s - i + x * 2 + 1
                if left_child < including_range:
                    if array[left_child] > array[root]:
                        swap = array[left_child]
                        array[left_child] = array[root]
                        array[root] = swap
                if right_child < including_range:
                    if array[right_child] > array[root]:
                        swap = array[right_child]
                        array[right_child] = array[root]
                        array[root] = swap
            l -= 1
            s -= i
            i = i // 2
        including_range -= 1
        swap = array[0]
        array[0] = array[including_range]
        array[including_range] = swap
