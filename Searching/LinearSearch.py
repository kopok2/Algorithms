def linear_search(array, value):
    for x in range(len(array)):
        if array[x] == value:
            return x
    return -1
