class Node:
    def __init__(self, key, left=None, right=None):
        self.value = key
        self.left = left
        self.right = right


def inorder_traversal(nodes):
    item = []
    if nodes.left is not None:
        item = item + inorder_traversal(nodes.left)
    item = item + [nodes.value]
    if nodes.right is not None:
        item = item + inorder_traversal(nodes.right)
    return item


def preorder_traversal(nodes):
    item = []
    item = item + [nodes.value]
    if nodes.left is not None:
        item = item + preorder_traversal(nodes.left)
    if nodes.right is not None:
        item = item + preorder_traversal(nodes.right)
    return item


def postorder_traversal(nodes):
    item = []
    if nodes.left is not None:
        item = item + postorder_traversal(nodes.left)
    if nodes.right is not None:
        item = item + postorder_traversal(nodes.right)
    item = item + [nodes.value]
    return item


def levelorder_traversal(tree, level):
    current_level = 0
    item = []
    if current_level == level:
        item = item + [tree.value]
    if current_level < level:
        if tree.left is not None:
            item = item + levelorder_traversal(tree.left, level-1)
        if tree.right is not None:
            item = item + levelorder_traversal(tree.right, level-1)
    return item


def insert_binary_search_tree(tree, item):
    if tree is None:
        return Node(item)
    if item >= tree.value:
        if tree.right is None:
            tree.right = Node(item)
        else:
            insert_binary_search_tree(tree.right, item)
    else:
        if tree.left is None:
            tree.left = Node(item)
        else:
            insert_binary_search_tree(tree.left, item)
    return tree
