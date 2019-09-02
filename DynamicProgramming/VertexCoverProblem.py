# coding=utf-8
"""Vertex cover problem dynamic programming solution Python implementation."""


class Node:
    def __init__(self, value):
        self.value = value
        self.vc = 0
        self.left = None
        self.right = None


def mvcp(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 0
    if root.vc != 0:
        return root.vc
    size_incl = 1 + mvcp(root.left) + mvcp(root.right)
    size_excl = 0
    if root.left:
        size_excl += 1 + mvcp(root.left.left) + mvcp(root.left.right)
    if root.right:
        size_excl += 1 + mvcp(root.right.left) + mvcp(root.right.right)
    root.vc = min(size_incl, size_excl)
    return root.vc


if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    print(mvcp(root))
