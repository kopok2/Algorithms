# coding=utf-8
"""Find minimum spanning tree for given graph."""

from operator import itemgetter

def add_to_set(settt, vals):
    start = -1
    stop = -1
    for x in range(len(settt)):
        if vals[1] in settt[x]:
            start = x
            break
    for x in range(len(settt)):
        if vals[2] in settt[x]:
            stop = x
            break
    if start >= 0 and stop >=0:
        if start != stop:
            settt[start] += settt[stop]
            settt.remove(settt[stop])
        else:
            return False
    elif start >= 0:
        settt[start].append(vals[2])
    elif stop >= 0:
        settt[stop].append(vals[1])
    else:
        settt.append([vals[1], vals[2]])
    return True


def minimum_spanning_tree(vertices):

    vertices.sort(key=itemgetter(0), reverse=True)
    connected = []
    selected = []
    while vertices:
        vert = vertices.pop()
        # cycle detection using disjoint set
        if add_to_set(connected, vert):
            selected.append(vert)
    return selected


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
