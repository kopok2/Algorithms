# coding=utf-8
"""Dynamic programming (tabulation) Fibonacci series generator."""


def fibonacci(x):
    mem = [None for y in range(x)]
    mem[0] = mem[1] = 1
    for y in range(2, x):
        mem[y] = mem[y - 2] + mem[y - 1]
    return mem


if __name__ == "__main__":
    print(fibonacci(100))
