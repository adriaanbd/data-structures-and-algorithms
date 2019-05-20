from node import Node


def create_linked_list(input_list: list) -> Node:
    """
    Creates a linked list from list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    input_list = input_list[:]
    if not len(input_list):
        return None
    head = Node(input_list.pop(0))
    current_node = head
    while len(input_list):
        current_node.next = Node(input_list.pop(0))
        current_node = current_node.next
    return head


def create_linked_list_better(input_list, head=None, tail=None):
    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next
    return head


# Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + e)


# import pdb; pdb.set_trace()
input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list_better(input_list)
test_function(input_list, head)