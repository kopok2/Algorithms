# coding=utf-8
"""M Coloring Graph Problem Backtracking Algorithm solution Python implementation."""

V = 4  # vertices count


def is_safe(v, graph, color, c):
    for i in range(V):
        if graph[v][i] and c == color[i]:
            return False
    return True


def graph_coloring_util(graph, m, color, v):
    if v == V:
        return True
    for c in range(1, m + 1):
        if is_safe(v, graph, color, c):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True
            else:
                color[v] = 0
    return False


def graph_coloring(graph, m):
    color = [0] * V
    if graph_coloring_util(graph, m, color, 0):
        print(color)
    else:
        print("No solution exists.")


if __name__ == "__main__":
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0]]
    m = 3
    graph_coloring(graph, m)
