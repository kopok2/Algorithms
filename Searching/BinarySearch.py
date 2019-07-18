def binary_search(array, value):
    left = 0
    right = len(array) - 1
    while right - left:
        mid = left + ((right - left) // 2)
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            right = mid
        else:
            left = mid
        if right - left == 1:
            left = right
            mid = left + ((right - left) // 2)
            if array[mid] == value:
                return mid
            if array[mid - 1] == value:
                return mid - 1
    return -1
