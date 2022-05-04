# python3


class Vertex:
    def __init__(self, key):
        self.key = key
        self.edges = []
        self.distance = -1
        self.prev = None

    def connect(self, other):
        self.edges.append(other)

    def __repr__(self):
        return '(key: {}, edges: {}, distance: {})'.format(self.key + 1, [v.key for v in self.edges], self.distance)


def bfs(s):
    s.distance = 0
    queue = [s]
    while len(queue) > 0:
        v = queue.pop(0)
        for w in v.edges:
            if w.distance == -1:
                queue.append(w)
                w.distance = v.distance + 1
                w.prev = v


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
    for _ in range(m):
        u, v = [int(i) - 1 for i in input().split(' ')]
        graph[u].connect(graph[v])
        graph[v].connect(graph[u])
    u, v = [int(i) - 1 for i in input().split(' ')]
    bfs(graph[u])
    shortest_path = reconstruct_path(graph[u], graph[v])
    distance = len(shortest_path)
    distance = -1 if distance == 0 else distance
    print(distance)


if __name__ == '__main__':
    main()
