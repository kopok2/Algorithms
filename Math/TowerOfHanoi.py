# coding=utf-8
"""Tower of Hanoi algorithm Python implementation."""


def th(n, f, t, a):
    if n == 1:
        print("Move disk 1 from {0} to {1}".format(f, t))
    else:
        th(n - 1, f, a, t)
        print("Move disk {0} from {1} to {2}".format(n, f, t))
        th(n - 1, a, t, f)


if __name__ == '__main__':
    n = 2
    th(n, "A", "B", "C")
