# coding=utf-8
"""Dijkstra shortest path alogrithm Python implementation."""

from operator import itemgetter


def dijkstra(edges, starting, directed=False):
    if not directed:
        edges += [[x[1], x[0], x[2]] for x in edges]
    edges.sort(key=itemgetter(2), reverse=True)
    inf = edges[0][2] * len(edges)
    distances = [inf for x in range(max([e[1] for e in edges]))]
    distances[starting - 1] = 0
    to_visit = [starting]
    visited = []
    while to_visit:
        visiting = to_visit.pop(0)
        if not visiting in visited:
            visited.append(visiting)
            for edge in edges:
                if edge[0] == visiting:
                    distances[edge[1] - 1] = min(distances[edge[1] - 1], distances[edge[0] - 1] + edge[2])
                    to_visit.append(edge[1])
    return distances


if __name__ == "__main__":
    # src   dest  weight
    edges = \
        [[7, 6, 1 ],
         [8, 2, 2 ],
         [6, 5, 2 ],
         [0, 1, 4 ],
         [2, 5, 4 ],
         [8, 6, 6 ],
         [2, 3, 7 ],
         [7, 8, 7 ],
         [0, 7, 8 ],
         [1, 2, 8 ],
         [3, 4, 9 ],
         [5, 4, 10],
         [1, 7, 11],
         [3, 5, 14]]
    edges = [[x[0] + 1, x[1] + 1, x[2]] for x in edges]
    for i, x in enumerate(dijkstra(edges, 1)):
        print(i, x)
