# python3
class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def in_order(root):
    stack = []
    current = root
    done = False
    while not done:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                print(current.key, end=' ', flush=True)
                current = current.right
            else:
                done = True


def pre_order(root):
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        print(current.key, end=' ', flush=True)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)


def post_order(root):
    stack1 = []
    stack2 = []
    stack1.append(root)
    while len(stack1) > 0:
        current = stack1.pop()
        stack2.append(current)

        if current.left is not None:
            stack1.append(current.left)
        if current.right is not None:
            stack1.append(current.right)
    while len(stack2) > 0:
        print(stack2.pop().key, end=' ', flush=True)


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
