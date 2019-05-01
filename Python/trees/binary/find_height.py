"""
Write a function to find the height of this binary tree!
    A
   / \
  B   C
 / \
D   E
     \
      F
"""


def Binary_Tree_Height(tree):
    """
    Find the height of a binary tree

    Args:
       tree(object): Input binary tree
    Returns:
       int: The height of the tree
    """
    pass


# Test Case
class Tree:
    def __init__(self, value, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.value)


f = Tree("F")
e = Tree("E", None, f)

d = Tree("D")
b = Tree("B", d, e)

c = Tree("C")
a = Tree("A", b, c)

my_tree = a

print("Pass" if (4 == Binary_Tree_Height(my_tree)) else "Fail")