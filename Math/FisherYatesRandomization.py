# coding=utf-8
"""Fisher-Yates algorithm for random permutation Python implementation."""

from random import randrange


def randomize(array):
    for i in range(len(array) - 1, 0, -1):
        j = randrange(0, 10*20) % (i + 1)
        array[i], array[j] = array[j], array[i]
    return array


if __name__ == '__main__':
    array = [randrange(1, 100) for x in range(randrange(10, 50))]
    print(array)
    print(randomize(array))
