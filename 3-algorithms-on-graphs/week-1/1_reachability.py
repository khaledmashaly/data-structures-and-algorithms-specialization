# python3
class Cell:
    def __init__(self, key):
        self.key = key
        self.adjacent = []
        self.visited = False
        self.cc = None

    def add(self, other):
        self.adjacent.append(other)

    def __repr__(self):
        return '( key: {}, adjacent: {} )'.format(self.key, [cell.key for cell in self.adjacent])


def connect(first, second):
    first.add(second)
    second.add(first)


def explore(v, cc):
    v.visited = True
    v.cc = cc
    for w in v.adjacent:
        if not w.visited:
            explore(w, cc)


def dfs(maze):
    for key, v in maze.items():
        v.visited = False
    cc = 1
    for key, v in maze.items():
        if not v.visited:
            explore(v, cc)
            cc += 1
    return maze


def is_reachable(maze, x, y):
    maze = dfs(maze)
    output = 1 if maze[x].cc == maze[y].cc else 0
    print(output)


def main():
    n, m = [int(i) for i in input().split(' ')]
    maze = {i: Cell(i) for i in range(1, n + 1)}
    for i in range(m):
        u, v = [int(i) for i in input().split(' ')]
        connect(maze[u], maze[v])
    # print(maze)
    x, y = [int(i) for i in input().split(' ')]
    is_reachable(maze, x, y)


if __name__ == '__main__':
    main()
