"""
Explore Binary Search Tree

Now try implementing a BST on your own.
You'll use the same Node class as before:

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

This time, you'll implement search() and insert().
You should rewrite search() and not use your code from the last exercise so it
takes advantage of BST properties. Feel free to make any helper functions you
feel like you need, including the print_tree() function from earlier for
debugging.

You can assume that two nodes with the same value
won't be inserted into the tree.

Beware of all the complications discussed in the videos!
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
print ("Pass" if tree.search(4) else "Fail")
print ("Pass" if not tree.search(6) else "Fail")
