"""
Explore Binary Trees

Now, it's your turn! Your goal is to create your own binary tree.
You should start with the most basic building block:

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

Every node has some value, and pointers to left and right children.

You'll need to implement two methods: search(),
which searches for the presence of a node in the tree,
and print_tree(), which prints out the values of tree nodes
in a pre-order traversal.

You should attempt to use the helper methods provided to create
recursive solutions to these functions.

Let's get started!
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
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return ""

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
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