# python3
class Tree:
    def __init__(self):
        self.root = None
        self.descendants = []

    def add_descendant(self, descendant):
        self.descendants.append(descendant)


class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

    def add_children(self, *children):
        self.children.extend(children)


def tree_height(node):
    if len(node.children) is 0:
        return 1
    else:
        max_child_height = max([tree_height(child) for child in node.children])
        # max_child_height = 0
        # for child in node.children:
        #     child_height = tree_height(child)
        #     if child_height > max_child_height:
        #         max_child_height = child_height
        return max_child_height + 1


def bf_traversal(root):
    tree_queue = [root]
    height = 0

    while len(tree_queue) > 0:

        for i in range(0, len(tree_queue)):
            node = tree_queue.pop(0)
            if len(node.children) > 0:
                tree_queue.extend(node.children)

        height += 1

    return height

node_number = int(input())
hierarchy = input().split(' ')
hierarchy = [int(i) for i in hierarchy]

tree = Tree()

# populate the tree
for n in range(0, node_number):
    tree.add_descendant(Node(n))

# assign children to corresponding parent
for child_number, parent_number in enumerate(hierarchy):
    if parent_number > -1:
        parent = tree.descendants[parent_number]
        child = tree.descendants[child_number]
        parent.add_children(child)
    else:
        root = tree.descendants[child_number]
        tree.root = root

print(bf_traversal(tree.root))
