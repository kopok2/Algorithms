# coding=utf-8
"""Floyd-Warshall algorithm Python implementation."""


def floyd_warshall(graph):
    """Find pairwise shortest paths in weighted directed graph.

    Args:
        graph: n x n table of distances between nodes (0 for main diagonal, -1 if no connection).

    Returns:
        table with pairwise shortest distances between nodes.
    """
    dist = [[999999 for x in range(len(graph[0]))] for y in range(len(graph))]
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            dist[x][y] = graph[x][y]
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


if __name__ == "__main__":
    INF = 999999
    graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
    ]
    for d in floyd_warshall(graph):
        print(d)
