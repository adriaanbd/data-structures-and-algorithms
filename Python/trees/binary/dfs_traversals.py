"""
DFS Workbook

In this workbook we will try out the three main types of
Depth First Binary Tree Traversal: Pre-order, In-order and Post-order.
In each of the cells below you will implement a pre, in and post order
traversal of the tree by printing the node's value when you visit it.

Before we traverse anything though, we need a binary tree to traverse.
The following code creates implements a simple Tree class and creates a tree
called my_tree with the following stucture:

    A
   / \
  B   C
 / \
D   E
     \
      F
"""


class Tree:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.value)


def print_tree_preorder(tree):
    """
    Implement a pre-order traversal here

    Args:
       tree(object): A binary tree input
    Returns:
       None
    """


def print_tree_inorder(tree):
    """
    Implement a in-order traversal here

    Args:
       tree(object): A binary tree input
    Returns:
       None
    """


def print_tree_postorder(tree):
    """
    Implement a post-order traversal here

    Args:
       tree(object): A binary tree input
    Returns:
       None
    """


f = Tree("F")
e = Tree("E", None, f)

d = Tree("D")
b = Tree("B", d, e)

c = Tree("C")
a = Tree("A", b, c)

my_tree = a

print_tree_preorder(my_tree)
print_tree_inorder(my_tree)
print_tree_postorder(my_tree)