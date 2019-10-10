# coding=utf-8
"""Tree check for graph."""


def is_tree(edges, vertex_cnt):
    graph = [[] for x in range(vertex_cnt)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])
    comp = [0] * vertex_cnt
    to_visit = graph[0]
    while to_visit:
        visiting = to_visit.pop(-1)
        if not comp[visiting - 1]:
            comp[visiting - 1] = 1
            to_visit += graph[visiting - 1]
    return sum(comp) == vertex_cnt and len(edges) == vertex_cnt - 1


if __name__ == '__main__':
    edges = [[2, 1], [1, 3], [1, 4], [4, 5]]
    print(is_tree(edges, 5))

    edges = [[2, 1], [1, 3], [1, 4], [4, 5], [3, 2]]
    print(is_tree(edges, 5))
