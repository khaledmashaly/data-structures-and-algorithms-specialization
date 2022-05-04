# python3
import sys


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
        return self.key < other.key

    def __repr__(self):
        return '(key: {}, edges: {}, dist: {})'.format(self.key, [e.v.key for e in self.edges], self.dist)


class Edge:
    def __init__(self, v, weight):
        self.v = v
        self.weight = weight


def negative_cycles(graph, length, s):
    s = graph[s]
    s.dist = 0
    a = []
    for i in range(length):
        for u in graph:
            for edge in u.edges:
                w = edge.v
                if w.dist > u.dist + edge.weight:
                    w.dist = u.dist + edge.weight
                    w.prev = u
                    if i == length - 1:
                        a.append(w)
    return graph, a


def bfs(graph, a):
    for s in a:
        if s.dist > float('-Inf'):
            s.dist = float('-Inf')
            queue = [s]
            while len(queue) > 0:
                v = queue.pop(0)
                for edge in v.edges:
                    w = edge.v
                    if w.dist > float('-Inf'):
                        queue.append(w)
                        w.dist = float('-Inf')
                        w.prev = v
    graph.sort()
    for v in graph:
        if v.dist == float('Inf'):
            print('*')
        elif v.dist == float('-Inf'):
            print('-')
        else:
            print(v.dist)


def main():
    n, m = [int(i) for i in input().split(' ')]
    graph = [Vertex(i) for i in range(n)]
    for i in range(m):
        u, v, w = [int(j) for j in input().split(' ')]
        graph[u - 1].connect(graph[v - 1], w)
    s = int(input())
    graph, a = negative_cycles(graph, n, s - 1)
    bfs(graph, a)


if __name__ == '__main__':
    main()
