# coding=utf-8
"""Pascal's Triangle algorithm Python implementation."""


def pascal(n):
    for line in range(1, n + 1):
        c = 1
        for i in range(1, line + 1):
            print(c, end=" ")
            c = (c * (line - i)) // i
        print("\n")


if __name__ == '__main__':
    pascal(10)
