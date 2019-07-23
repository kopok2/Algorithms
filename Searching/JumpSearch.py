import math

def jump_search(array, value):
    step_size = int(math.sqrt(len(array)))
    interval = 0
    for x in range(step_size, len(array), step_size):
        if array[x - step_size] < value and array[x] >= value:
            interval = x
            break
    for x in range(interval - step_size, interval+1):
        if array[x] == value:
            return x
    return -1
