# coding=utf-8
"""Largest independent set problem dynamic programming solution Python implementation."""


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.liss = 0


def liss(root):
    if not root:
        return 0
    elif root.liss:
        return root.liss
    elif not root.left and not root.right:
        root.liss = 1
        return 1
    else:
        liss_excl = liss(root.left) + liss(root.right)
        liss_incl = 1
        if root.left:
            liss_incl += liss(root.left.left) + liss(root.left.right)
        if root.right:
            liss_incl += liss(root.right.left) + liss(root.right.right)
        root.liss = max(liss_incl, liss_excl)
        return root.liss


if __name__ == "__main__":
    root = Node()
    root.left = Node()
    root.left.left = Node()
    root.left.right = Node()
    root.left.right.left = Node()
    root.left.right.right = Node()
    root.right = Node()
    root.right.right = Node()
    print(liss(root))
