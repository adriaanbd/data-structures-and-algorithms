"""
TODO: implement BST main operations
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Build out the insert function
        pass

    def search(self, find_val):
        # Build out the search function
        return False


# Test Cases
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
print("Pass" if tree.search(4) else "Fail")
print("Pass" if not tree.search(6) else "Fail")
