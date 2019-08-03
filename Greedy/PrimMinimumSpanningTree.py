# coding=utf-8
"""Prim's minimum spanning tree implementation."""

from operator import itemgetter


def minimum_spanning_tree(vertices):
    srcs = [x[1] for x in vertices]
    dests = [x[2] for x in vertices]
    inf = max([x[0] for x in vertices]) + 1
    vertex = [[x, inf, -1] for x in list(set(srcs + dests))]
    vertex[0][1] = 0
    included = []
    edges = []
    while vertex:
        vertex.sort(key=itemgetter(1))
        adding = vertex.pop(0)
        if adding[2] >= 0:
            edges.append((adding[1], adding[2], adding[0]))
        included.append(adding[0])
        print(vertex)
        for vert in vertices:
            if vert[1] in included and vert[2] not in included or vert[1] not in included and vert[2] in included:
                for e in vertex:
                    if e[0] == vert[1] and vert[0] < e[1]:
                        e[1] = vert[0]
                        e[2] = vert[2]
                    elif e[0] == vert[2] and vert[0] < e[1]:
                        e[1] = vert[0]
                        e[2] = vert[1]
    return edges


if __name__ == "__main__":
    # Weight   Src    Dest
    graph = \
    [[1 ,        7,      6],
    [2 ,        8,      2],
    [2 ,        6,      5],
    [4 ,        0,      1],
    [4 ,        2,      5],
    [6 ,        8,      6],
    [7 ,        2,      3],
    [7 ,        7,      8],
    [8 ,        0,      7],
    [8 ,        1,      2],
    [9 ,        3,      4],
    [10,        5,      4],
    [11,        1,      7],
    [14,        3,      5]]
    print(minimum_spanning_tree(graph))
