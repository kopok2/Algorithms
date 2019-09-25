# coding=utf-8
"""Biased to fair coin conversion."""

import random


def coin():
    return random.randrange(100) > 10


def fair_coin():
    v1 = coin()
    v2 = coin()
    if v1 and not v2:
        return 1
    elif v2 and not v1:
        return 0
    else:
        return fair_coin()


if __name__ == '__main__':
    o = 0
    z = 0
    for x in range(1000000):
        if fair_coin():
            o += 1
        else:
            z += 1
    print(o, z, o / z)
