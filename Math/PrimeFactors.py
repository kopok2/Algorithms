# coding=utf-8
"""Prime factor algorithm Python implementation."""

import math


def prime_factors(n):
    if x <= 2:
        return [2]
    result = []
    while not (n % 2):
        result.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while not (n % i):
            result.append(i)
            n //= i
    if n > 2:
        result.append(n)
    return result


if __name__ == '__main__':
    for x in range(1000000):
        print(x, prime_factors(x))
