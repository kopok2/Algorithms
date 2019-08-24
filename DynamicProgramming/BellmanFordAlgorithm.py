# coding=utf-8
"""Bellman-Ford shortest path algorithm Python implementation."""


def bellman_ford_shortest_path(edges, src):
    vertices_count = len(list(set([e[0] for e in edges] + [e[1] for e in edges])))
    distances = [vertices_count * len(edges) if x != src else 0 for x in range(vertices_count)]
    for x in range(vertices_count - 1):
        for edge in edges:
            if distances[edge[1]] > distances[edge[0]] + edge[2]:
                distances[edge[1]] = distances[edge[0]] + edge[2]
    for edge in edges:
        if distances[edge[1]] > distances[edge[0]] + edge[2]:
            return False
    return distances


if __name__ == "__main__":
    edges = [
        [0, 1, -1],
        [0, 2, 4],
        [1, 2, 3],
        [1, 3, 2],
        [1, 4, 2],
        [3, 2, 5],
        [3, 1, 1],
        [4, 3, -3]
    ]
    print(bellman_ford_shortest_path(edges, 0))
