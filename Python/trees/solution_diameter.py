# This solution is not mine, it was provided by Udacity's Data Structures and Algorithms Nanodegree. Keeping it here for further reference.

from queue import Queue


class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree 
    """
    index = 0
    length = len(arr)
    
    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTreeNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)
    
    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1
        
        if left_child is not None:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)
        
        right_child = arr[index]
        index += 1
        
        if right_child is not None:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root


# Solution
def diameter_of_binary_tree(root):
    return diameter_of_binary_tree_func(root)[1]


def diameter_of_binary_tree_func(root):
    """
    Diameter for a particular BinaryTree Node will be:
        1. Either diameter of left subtree
        2. Or diameter of a right subtree
        3. Sum of left-height and right-height
    :param root:
    :return: [height, diameter]
    """
    if root is None:    # base case
        return 0, 0

    left_height, left_diameter = diameter_of_binary_tree_func(root.left)
    right_height, right_diameter = diameter_of_binary_tree_func(root.right)

    current_height = max(left_height, right_height) + 1  # always from perspective of root
    height_diameter = left_height + right_height  # height from leaf to leaf
    current_diameter = max(left_diameter, right_diameter, height_diameter)

    return current_height, current_diameter


# arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
arr = [5, 3, 7, 1, 4, None, 10, None, None, None, 6, None, None, None, None]
root = convert_arr_to_binary_tree(arr)

output = diameter_of_binary_tree(root)
print(output)
