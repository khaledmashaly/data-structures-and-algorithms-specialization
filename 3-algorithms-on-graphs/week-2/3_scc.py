# python3


class Vertex:
    def __init__(self, key):
        self.key = key
        self.edges = []
        self.visited = False
        self.post = 0
        self.scc = 0

    def connect(self, other):
        self.edges.append(other)

    def __repr__(self):
        return '(key: {}, edges: {}, post: {})'.format(self.key + 1, [v.key for v in self.edges], self.post)

    def __lt__(self, other):
        return self.post > other.post


def dfs(graph, output=False):
    clock = 0
    scc = 0

    for v in graph:
        v.visited = False

    for v in graph:
        if not v.visited:
            stack = [v]
            while len(stack) > 0:
                current = stack[-1]
                current.visited = True
                current.scc = scc

                for vertex in current.edges:
                    if not vertex.visited:
                        stack.append(vertex)
                        break
                else:
                    current.post = clock
                    clock += 1
                    stack.pop()
            scc += 1
    if output:
        print(scc)
    else:
        return graph


def strongly_cc(graph_r, graph):
    graph_r = dfs(graph_r)
    graph = list(zip(graph_r, graph))
    graph.sort()
    graph_r, graph = zip(*graph)
    dfs(graph, True)


def main():
    n, m = [int(i) for i in input().split(' ')]
    graph = [Vertex(i) for i in range(n)]
    graph_r = [Vertex(i) for i in range(n)]
    for i in range(m):
        u, v = [int(i) - 1 for i in input().split(' ')]
        graph[u].connect(graph[v])
        graph_r[v].connect(graph_r[u])
    strongly_cc(graph_r, graph)


if __name__ == '__main__':
    main()
