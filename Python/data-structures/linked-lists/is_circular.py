from singly_linked_list import LinkedList


def is_circular(linked_list: LinkedList) -> bool:
    """
    Determine wether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """
    slow_runner = linked_list.head
    fast_runner = linked_list.head

    while fast_runner.next and fast_runner.next.next:
        if slow_runner.next == slow_runner:
            return True

        fast_runner = fast_runner.next.next
        slow_runner = slow_runner.next
        if slow_runner == fast_runner:
            return True

    return False


list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next

# last node points to head.next
node.next = loop_start

# Test Cases

print("Pass" if is_circular(list_with_loop) is True else "Fail")
print("Pass" if is_circular(LinkedList([-4, 7, 2, 5, -1])) is False else "Fail")
print("Pass" if is_circular(LinkedList([1])) is False else "Fail")
