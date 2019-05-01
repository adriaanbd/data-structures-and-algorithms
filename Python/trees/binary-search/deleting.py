"""
Practicing Adding Deletion

You have just added the abiliy to insert and search on the tree lets take it
one step farther by having you add the ability to delete of the tree as well.
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
        # Use your old insert function
        pass

    def search(self, find_val):
        # Use your old search function
        return False

    def delete(self, del_val):
        # Implement a delete function
        pass


# Test cases
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

# Delete elements
tree.delete(5)

# Should be False
print("Pass" if not tree.search(5) else "Fail")
