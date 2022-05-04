# python3
import sys


class Vertex:
    def __init__(self, key):
        self.key = key
        self.edges = []
        self.set = 0
        self.prev = None

    def connect(self, other):
        self.edges.append(other)

    def __repr__(self):
        return '(key: {}, edges: {}, distance: {})'.format(self.key + 1, [v.key for v in self.edges], self.distance)


def bfs(s):
    s.set = 1
    queue = [s]
    while len(queue) > 0:
        v = queue.pop(0)
        for w in v.edges:
            if w.set == 0:
                queue.append(w)
                w.set = 1 if v.set == 2 else 2
                w.prev = v
            elif w.set == v.set:
                print(0)
                sys.exit(0)


def reconstruct_path(s, u):
    result = []
    while u is not s:
        if u.prev is None:
            return []
        result.append(u)
        u = u.prev
    return result


def main():
    n, m = [int(i) for i in input().split(' ')]
    graph = [Vertex(i) for i in range(n)]
    for i in range(m):
        u, v = [int(i) - 1 for i in input().split(' ')]
        graph[u].connect(graph[v])
        graph[v].connect(graph[u])
    bfs(graph[0])
    print(1)


if __name__ == '__main__':
    main()
