# python3
import sys
import heapq


class Vertex:
    def __init__(self, key):
        self.key = key + 1
        self.edges = []
        self.dist = float('Inf')
        self.prev = None

    def connect(self, other, weight):
        edge = Edge(other, weight)
        self.edges.append(edge)

    def __lt__(self, other):
        return self.dist < other.dist

    def __repr__(self):
        return '(key: {}, edges: {}, dist: {})'.format(self.key, [e.v.key for e in self.edges], self.dist)


class Edge:
    def __init__(self, v, weight):
        self.v = v
        self.weight = weight


def dijkstra(graph, s, d):
    s = graph[s]
    d = graph[d]
    s.dist = 0
    heapq.heapify(graph)
    while len(graph) > 0:
        v = heapq.heappop(graph)
        for edge in v.edges:
            w = edge.v
            if w.dist > v.dist + edge.weight:
                w.dist = v.dist + edge.weight
                w.prev = v
                heapq.heapify(graph)
    return d.dist


def main():
    n, m = [int(i) for i in input().split(' ')]
    graph = [Vertex(i) for i in range(n)]
    for i in range(m):
        u, v, w = [int(j) for j in input().split(' ')]
        graph[u - 1].connect(graph[v - 1], w)
    s, d = [int(i) for i in input().split(' ')]
    dist = dijkstra(graph, s - 1, d - 1)
    dist = dist if dist != float('Inf') else -1
    print(dist)


if __name__ == '__main__':
    main()
