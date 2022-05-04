# python3
class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def in_order(tree):
    stack = []
    done = False
    while not done:
        if tree is not None:
			stack.append(tree)
			tree = tree.left
		else:
			if len(s) > 0:
				node = stack.pop()
				print(node, end=' ', flush=True)
				tree = node.right
			else:
				done = True


def pre_order(tree):
    if tree is None:
        return
    print(tree.key, end=' ', flush=True)
    pre_order(tree.left)
    pre_order(tree.right)


def post_order(tree):
    if tree is None:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.key, end=' ', flush=True)


def main():
    n = int(input())
    nodes = []
    for i in range(n):
        node_info = [int(i) for i in input().split(' ')]
        node = Node(*node_info)
        nodes.append(node)
    for node in nodes:
        node.left = nodes[node.left] if node.left != -1 else None
        node.right = nodes[node.right] if node.right != -1 else None
    in_order(nodes[0])
    print('')
    pre_order(nodes[0])
    print('')
    post_order(nodes[0])


main()
