def interpolation_search(array, value):
    lo = 0
    hi = len(array) - 1
    while lo <= hi and value >= array[lo] and value <= array[hi]:
        if lo == hi:
            if array[lo] == value:
                return lo
            else:
                return -1
        if array[hi] == array[lo]:
            if array[hi] == value:
                return hi
            else:
                return -1
        pos = lo + int((hi - lo)/(array[hi] - array[lo])*(value - array[lo]))
        if array[pos] == value:
            return pos
        if array[pos] < value:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1
