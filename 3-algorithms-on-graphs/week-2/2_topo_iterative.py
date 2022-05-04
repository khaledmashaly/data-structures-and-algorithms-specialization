# python3


class Vertex:
    def __init__(self, key):
        self.key = key
        self.edges = []
        self.visited = False
        self.pre = 0
        self.post = 0
        self.scc = 0

    def connect(self, other):
        self.edges.append(other)

    def __repr__(self):
        return '(key: {}, pre: {}, post: {})'.format(self.key + 1, self.pre, self.post)

    def __lt__(self, other):
        return self.post > other.post


def toposort(graph):
    for v in graph:
        v.visited = False
    order = []
    for v in graph:
        if not v.visited:
            stack = [v]
            while len(stack) > 0:
                current = stack[-1]
                for vertex in current.edges:
                    if not vertex.visited:
                        stack.append(vertex)
                        break
                else:
                    current.visited = True
                    stack.pop()
                    order.append(current.key + 1)
    print(*list(reversed(order)))


def main():
    n, m = [int(i) for i in input().split(' ')]
    graph = [Vertex(i) for i in range(n)]
    for i in range(m):
        u, v = [int(i) - 1 for i in input().split(' ')]
        graph[u].connect(graph[v])
    toposort(graph)


if __name__ == '__main__':
    main()
