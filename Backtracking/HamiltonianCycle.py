# coding=utf-8
"""Hamiltonian Cycle Backtracking finding algorithm Python implementation."""

V = 5  # vertices count


def is_safe(v, graph, path, pos):
    if not graph[path[pos - 1]][v]:
        return False
    for i in range(pos):
        if path[i] == v:
            return False
    return True


def hc_util(graph, path, pos):
    if pos == V:
        return graph[path[pos - 1]][path[0]] == 1
    for v in range(1, V):
        if is_safe(v, graph, path, pos):
            path[pos] = v
            if hc_util(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False


def hc(graph):
    path = [-1] * V
    path[0] = 0
    if hc_util(graph, path, 1):
        print(path)
    else:
        print("No solution exists.")


if __name__ == "__main__":
    graph = [[0, 1, 0, 1, 0],
             [1, 0, 1, 1, 1],
             [0, 1, 0, 0, 1],
             [1, 1, 0, 0, 1],
             [0, 1, 1, 1, 0]]
    hc(graph)
    graph = [[0, 1, 0, 1, 0],
             [1, 0, 1, 1, 1],
             [0, 1, 0, 0, 1],
             [1, 1, 0, 0, 0],
             [0, 1, 1, 0, 0]]
    hc(graph)
