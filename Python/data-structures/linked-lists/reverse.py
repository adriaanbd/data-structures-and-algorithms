from node import Node
from singly_linked_list import LinkedList


def reverse(llist: LinkedList) -> LinkedList:
    """
    Reverses a singly LinkedList without a tail by
    returning a new reversed LinkedList.
    """
    new_list = LinkedList()
    current_node = llist.head
    new_list.head = Node(current_node.value)
    while current_node:
        current_node = current_node.next
        if current_node:
            new_node = Node(current_node.value)
            new_node.next = new_list.head
            new_list.head = new_node
    return new_list


# Build the LinkedList with a python list:
llist = LinkedList()
python_list = [4, 2, 5, 1, -3, 0]
for value in python_list:
    llist.append(value)

# old linked list and new linked list to compare:
print(list(llist), reverse(llist))


# Test your function:

# reverse the original python list with reverse built-in method:
python_list.reverse()

# reversed python list and reversed linked list:
print(python_list, reverse(llist))

print("Pass" if python_list == list(reverse(llist)) else "Fail")
