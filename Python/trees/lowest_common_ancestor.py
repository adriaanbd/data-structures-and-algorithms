"""
Lowest Common Ancestor

Find the lowest common ancestor of two nodes in the tree.

Lowest common ancestor is the loweest node in which the two
provided nodes are decendents. For example in the tree below the
selected nodes of 1 and 6 give us a lowest common ancestor of 5 as
its the lowest amount in which both nodes are decendents.

Given the following binary tree:

    5
   / \
  2   6
 / \
1   3
     \
      4
"""

def lowest_common_ancestor(node):
    """
    Determine the lowest common ancestor

    Args:
       tree(object): A BST object
    Returns:
       int: Lowest shared ancestor
    """
    pass

# Test Cases

class Tree:
    def __init__(self, value, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.value)
        
f = Tree(4)
e = Tree(3, None, f)

d = Tree(1)
b = Tree(2, d, e)

c = Tree(6)
a = Tree(5, b, c)

my_tree = a

print("Pass" if 2 == lowest_common_ancestor(my_tree, 1, 4) else "Fail")