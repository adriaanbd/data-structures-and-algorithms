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
def path_from_root_to_node(root, data):
    """
    Assuming data as input to find the node
    The solution can be easily changed to find a node instead of data
    :param data:
    :return:
    """
    output = path_from_node_to_root(root, data)
    return list(reversed(output))


def path_from_node_to_root(root, data):
    if root is None:        # base case: found a leaf node
        return None

    if root.data == data:   # visit the node
        return [data]

    left_answer = path_from_node_to_root(root.left, data)
    if left_answer is not None:
        left_answer.append(root.data)
        return left_answer

    right_answer = path_from_node_to_root(root.right, data)
    if right_answer is not None:
        right_answer.append(root.data)
        return right_answer

    return None


# arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
arr = [5, 3, 7, 1, 4, None, 10, None, None, None, None, None, None, None, None]
root = convert_arr_to_binary_tree(arr)

output = path_from_root_to_node(root, 4)
print(output)
