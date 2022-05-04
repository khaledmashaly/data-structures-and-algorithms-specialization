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
        return self.dist < other.dist

    def __repr__(self):
        return '(key: {}, edges: {}, dist: {})'.format(self.key, [e.v.key for e in self.edges], self.dist)


class Edge:
    def __init__(self, v, weight):
        self.v = v
        self.weight = weight


def negative_cycles(vertices, length):
    s = vertices[0]
    s.dist = 0
    # for i in range(1, length):
    #     if len(s.edges) > 0:
    #         s.dist = 0
    #         break
    #     else:
    #         s = vertices[i]

    finished = False

    while not finished:
        finished = True
        for i in range(length):
            for u in vertices:
                for edge in u.edges:
                    w = edge.v
                    if w.dist > u.dist + edge.weight:
                        w.dist = u.dist + edge.weight
                        w.prev = u
                        if i == length - 1:
                            print(1)
                            sys.exit()
        for v in vertices:
            if v.dist == float('Inf') and len(v.edges) > 0:
                v.dist = 0
                finished = False
                break
    print(0)
    sys.exit()


def main():
    n, m = [int(i) for i in input().split(' ')]
    vertices = [Vertex(i) for i in range(n)]
    for i in range(m):
        u, v, w = [int(j) for j in input().split(' ')]
        vertices[u - 1].connect(vertices[v - 1], w)
    negative_cycles(vertices, n)


if __name__ == '__main__':
    main()
