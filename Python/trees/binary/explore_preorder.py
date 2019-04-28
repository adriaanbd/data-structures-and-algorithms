"""
Explore Binary Trees

Your goal is to create your own binary tree.
You should start with the most basic building block:

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

You'll need to implement two methods:
1. search() => searches for the presence of a node in the tree
2. print_tree() => prints out the values of tree nodes in a pre-order traversal.
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if self.root:
            return self.preorder_search(self.root, find_val)
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        if self.root:
            tree = self.preorder_print(self.root)
            return '-'.join(tree)
        return ""

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start.value == find_val:
            return True
        elif start.left or start.right:
            return self.preorder_search(start.left, find_val) or \
                self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal=[]):
        """Helper method - use this to create a
        recursive print solution."""
        traversal.append(str(start.value))
        if start.left or start.right:
            self.preorder_print(start.left, traversal)
            self.preorder_print(start.right, traversal)

        return traversal


# Test Cases
# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
print("Pass" if tree.search(4) else "Fail")
print("Pass" if not tree.search(6) else "Fail")
print("Pass" if (tree.print_tree() == '1-2-4-5-3') else "Fail")