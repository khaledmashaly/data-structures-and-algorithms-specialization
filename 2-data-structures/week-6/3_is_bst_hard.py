# python3
class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def in_order(root):
    if root is None:
        return []
    stack = []
    order = []
    current = root
    done = False
    while not done:
        if current is not None:
            stack.append(current)
            former = current
            current = former.left
            if (current is not None) and (former.key == current.key):
                return False
        else:
            if len(stack) > 0:
                current = stack.pop()
                order.append(current.key)
                current = current.right
            else:
                done = True
    return order


def is_bst(root):
    tree_order = in_order(root)
    if tree_order is False:
        return print('INCORRECT')
    ordered_tree = sorted(tree_order)
    if tree_order == ordered_tree:
        print('CORRECT')
    else:
        print('INCORRECT')


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
    root = nodes[0] if len(nodes) > 0 else None
    is_bst(root)


main()
