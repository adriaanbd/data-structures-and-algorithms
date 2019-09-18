"""
BST Check

Write a function to determine whether or not 
the input tree is a binary search tree.

    5
   / \
  2   6
 / \
1   3
     \
      4

Assumptions:

    Values bound by 0 < n < 100


"""


# Try Checking if it's a BST
def check_BST(tree):
    """
    Determine wether the input is a binary tree or not

    Args:
       tree(object): A BST object
    Returns:
       bool: True if it is a BST and False if not
    """
    return None


class Tree:
    def __init__(self, value, left=None, right=None):
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


​my_tree = a

# Test Cases
print("Pass" if check_BST(my_tree, lower, upper) else "Fail")
