def ternary_search(array, value):
    l = 0
    r = len(array)
    while r >= l:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if mid2 >= len(array):
            mid2 = len(array) - 1
        if value == array[mid1]:
            return mid1
        elif value == array[mid2]:
            return mid2
        elif value < array[mid1]:
            r = mid1 - 1
        elif value > array[mid2]:
            l = mid2 + 1
        elif r - l <= 1:
            return -1
        else:
            l = mid1 + 1
            r = mid2 - 1
    return -1
