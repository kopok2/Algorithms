# encoding-utf-8
"""Find kth smallets elements in array.

Using stack and deque with worst case O(n * k) time.
"""

import random
from collections import deque


def kth_smallest(array, k):
    size = len(array)
    smallest = deque()
    x = 0
    stack = []
    while x < size:
        if len(smallest) == 0:
            smallest.append(array[x])
        else:
            if array[x] < smallest[0]:
                if len(smallest) == k:
                    smallest.pop()
                smallest.appendleft(array[x])
            elif array[x] < smallest[-1]:
                if len(smallest) == k:
                    smallest.pop()
                while array[x] < smallest[-1]:
                    stack.append(smallest.pop())
                smallest.append(array[x])
                while stack:
                    smallest.append(stack.pop())
        x += 1
    print(smallest)
    return [smallest.popleft() for x in range(len(smallest))]


if __name__ == "__main__":
    array = [random.randrange(100) for x in range(100)]
    print(kth_smallest(array, 6))
    print(array)
    print(sorted(array))
