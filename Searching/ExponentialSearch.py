from InterpolationSearch import interpolation_search


def exponential_search(array, value):
    i = 1
    while i < len(array):
        if array[i] > value:
            return interpolation_search(array[i//2:i], value) + i//2
        i *= 2
    return interpolation_search(array[i//2:], value) + i//2
