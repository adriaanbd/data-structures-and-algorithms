from node import Node


def print_linked_list(current_node: Node):
    """
    Traverses a linked list from head to None and prints its value
    """
    if current_node:
        print(current_node.value)
        print_linked_list(current_node.next)
    return
