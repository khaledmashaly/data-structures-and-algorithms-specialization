# python3
import sys


class Vertex:
    def __init__(self, key):
        self.key = key
        self.edges = []
        self.visited = False

    def connect(self, other):
        self.edges.append(other)

    def __repr__(self):
        return '( key: {}, edges: {} )'.format(self.key, [vertex.key for vertex in self.edges])


def dfs(graph):
    order = []

    def explore(v):
        v.visited = True
        if len(v.edges) > 0:
            for w in v.edges:
                if not w.visited:
                    explore(w)
            order.append(v.key + 1)
        else:
            order.append(v.key + 1)

    for vertex in graph:
        vertex.visited = False
    for vertex in graph:
        if not vertex.visited:
            explore(vertex)

    print(*reversed(order))


def toposort(graph):
    dfs(graph)


def main():
    n, m = [int(i) for i in input().split(' ')]
    graph = [Vertex(i) for i in range(n)]
    for i in range(m):
        u, v = [int(i) - 1 for i in input().split(' ')]
        graph[u].connect(graph[v])
    toposort(graph)


if __name__ == '__main__':
    main()
