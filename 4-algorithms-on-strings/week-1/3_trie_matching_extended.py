# python3


class Node:
    def __init__(self, key):
        self.key = key
        self.prefix = False
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
            match = next((edge for edge in node.edges if edge.label == char), None)
            if match is None:
                new_node = Node(len(trie))
                trie.append(new_node)
                new_edge = Edge(char, new_node)
                node.edges.append(new_edge)
                node = new_edge.next
            else:
                node = match.next
        node.prefix = True
    return trie


def prefix_trie_matching(text, trie):
    text = list(text)
    symbol = text.pop(0)
    v = trie[0]
    spelled_pattern = ''
    while True:
        if len(v.edges) == 0 or v.prefix:
            return True
        match = next((edge for edge in v.edges if edge.label == symbol), None)
        if match is not None:
            if len(text) > 0:
                symbol = text.pop(0)
            else:
                symbol = None
            v = match.next
            spelled_pattern = spelled_pattern + match[0].label
        else:
            return False


def trie_matching(text, trie):
    for i in range(len(text)):
        match = prefix_trie_matching(text, trie)
        if match:
            print(i, end=' ')
        text = text[1:]


def main():
    text = input()
    n = int(input())
    patterns = []
    for _ in range(n):
        patterns.append(input())
    trie = construct_trie(patterns)
    trie_matching(text, trie)


if __name__ == '__main__':
    main()
