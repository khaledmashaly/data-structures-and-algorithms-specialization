# python3


class Node:
    def __init__(self, key):
        self.key = key
        self.edges = []


class Edge:
    def __init__(self, label, next_node):
        self.label = label
        self.next = next_node


def find_label(edges, label):
    for edge in edges:
        if edge.label == label:
            yield edge


def construct_trie(patterns):
    trie = [Node(0)]
    for pattern in patterns:
        node = trie[0]
        for char in pattern:
            match = list(find_label(node.edges, char))
            if len(match) == 0:
                new_node = Node(len(trie))
                trie.append(new_node)
                new_edge = Edge(char, new_node)
                node.edges.append(new_edge)
                node = new_edge.next
            else:
                node = match[0].next
    return trie


def construct_adjacency_list(trie):
    queue = [trie[0]]
    while len(queue) > 0:
        current = queue.pop(0)
        for edge in current.edges:
            queue.append(edge.next)
            print('{}->{}:{}'.format(current.key, edge.next.key, edge.label))


def main():
    n = int(input())
    patterns = []
    for i in range(n):
        patterns.append(input())
    trie = construct_trie(patterns)
    construct_adjacency_list(trie)


if __name__ == '__main__':
    main()
