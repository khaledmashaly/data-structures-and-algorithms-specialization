# python3
import math
from functools import reduce


class City:
    def __init__(self, key, x, y):
        self.key = key
        self.x = x
        self.y = y


class Edge:
    def __init__(self, u, w):
        self.u = u.key
        self.w = w.key
        self.dist = math.sqrt(math.pow(u.x - w.x, 2) + math.pow(u.y - w.y, 2))

    def __lt__(self, other):
        return self.dist < other.dist


def connect_cities(edges, n):

    parent = list(range(n))
    rank = [0] * n

    def find(i):
        if i != parent[i]:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        i_id = find(i)
        j_id = find(j)
        if i_id == j_id:
            return
        if rank[i_id] > rank[i_id]:
            parent[j_id] = i_id
        else:
            parent[i_id] = j_id
            if rank[i_id] == rank[j_id]:
                rank[j_id] += 1
        return

    x = []
    for edge in edges:
        u, w = edge.u, edge.w
        if find(u) != find(w):
            x.append(edge)
            union(u, w)
    distance = reduce(lambda a, b: a + b.dist, x, 0)
    return distance


def main():
    n = int(input())
    cities = []
    edges = []
    for i in range(n):
        city = City(i, *[int(i) for i in input().split(' ')])
        cities.append(city)
        for other_city in cities[:i]:
            edge = Edge(city, other_city)
            edges.append(edge)
    edges.sort()
    distance = connect_cities(edges, n)
    print('{:.10f}'.format(distance))


if __name__ == '__main__':
    main()
