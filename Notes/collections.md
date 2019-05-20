# Collections

A collection is a term used to describe a container of data, in a broad sense. That's why it is referred to as a very general structure, with the following **general** rules / characteristics:

* It is a group of data
* Without a specific order
* Not necessarily homogeneous or heterogeneous in object type

It's important to note the fact that although data structures are containers of data, they do have a specific way or organizing and grouping data; therefore, there are many data structures that are an extension of collections in the sense that they share some or most of the general rules of a collection, but they add or alter some of those rules / characteristics.

Let's look at some real-world examples of **specialized** collections.

## Lists vs Arrays

### Lists

A list is a collection with the following **specific** characteristics:

* Have a particular order
* Have no fixed length
* May or may not be next to another in memoery

And just like collections is a broad term, there are different types of lists.

### Arrays

An array is a list, with the following **specific** characteristic:

* Have indexes associating an item to its place in the array.
* All of the elements are of the same size

The reason is that when an array is created:

1. It is given an initial size, which implies:
   * The number of elements it can hold
   * How large the elements are

2. The computer then finds a block of memory and sets aside a *contiguous* space in memory for the array, which means: 
   * all elements are next to each other in memory.

Its important to note that having indexes make arrays a great choice in some situations, but a bad one in others. 

| Good                             | Why                                                          | Bad                    | Why                                                          |
| -------------------------------- | :----------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ |
| Accessing elements in the middle | By knowing the length of the array, a division by 2 will locate the middle index. | Insertion and Deletion | Inserting or deleting an element in the middle requires moving all of the elements to fill the extra space. |

### The Python List

A Python list is essentially implemented like an array, but behaves like a dynamic array. 

Some important characteristics:

* Is contiguous in memory
* Can be accessed using an index.
* Include `pop` and `append` methods to add and remove items

## Linked Lists

A linked list is an extension of a list, meaning that they share their general characteristics, but a linked list is not an array.

Some important characteristics: 

* Each element knows where the next element is, since it is connected to it.
* An element does not necessarily know how long the linked list is
* The elements in the list are not necessarily stored contiguously to each other

The main difference of a Linked List to an Array:

* The next element is determined by following the chain from one element to another, as opposed to determining location by index.

One of the great advantages of using a linked list over an array is that adding and removing elements is easier.

### Some Key Characteristics

1. Each node has 
   * a value / data that it holds
   * a  reference to the next node
2. The first element of the list if called the *head*
3. The linked list knows the location of the *head*
4. The *head* holds the reference to the next element, which will be used to initiate traversal.

### Implementation

With the key characteristics in place, we can define a Node class:

```Python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

With this we can: 

* instantiate a Node, 
* assign it to a variable named *head*
* instantiate another Node
* assign the *head.next* reference to the new Node

```Python
head = Node(10)
head.next = Node(20)
print(head.value) # returns 10
print(head.next.value) # returns 20
```

So far our list looks like this:  10 => 20

Nevertheless, we can take this idea further and extend the list to 10 => 20 => 30 => 40 => 50

```Python
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
print(head.next.next.value) # returns 30
print(head.next.next.next.value) # returns 40
print(head.next.next.next.next.value) # returns 50
```

### Traversal

#### Printing all the values in a linked list

The algorithm could look something like this:

1. Start with the head
2. Assign *current_node* to the *head*
3. If *current_node* is not None, continue, else exit
4. Print its value
5. Assign *current_node* to *current_node.next*
6. Repeat from Step 3

We can solve this using recursion:

```Python
def print_linked_list(current_node: Node):
    """
    Traverses a linked list from its head 
    and prints its value.
    """
    if current_node:
        print(current_node.value)
        print_linked_list(current_node.next)

print(print_linked_list(head))
```

Or iteration:

```Python
def print_linked_list(head):
    current_node = head
    
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next
        
print_linked_list(head)
```

#### Creating a linked list from an input list

The algorithm is similar to printing all of the values:

1. Return None if list is empty
2. Pop the first value out of the list
3. Assign *head* to this value
4. Assign *current_node* to *head*
5. While length of the list if greater than 0, execute from step 6 to 9
6. Pop the first value out of the list
7. Assign *current_node.next* to an instance of *Node* with this value
8. Assign *current_node* to *current_node.next*
9. Repeat from step 5
10. Return head

Translating it to code:

O(2n)

```Python
def create_linked_list(input_list: list) -> Node:
    if not len(input_list): # if list.empty?
        return None
    head = Node(input_list.pop(0)) # store head
    current_node = head 
    while len(input_list):
        current_node.next = Node(input_list.pop(0))
        current_node = current_node.next
    return head
```

A slightly better approach would be to have both a *head* and a *tail* reference:

O(n)

```Python
def create_better_linked_list(input_list, head=None, tail=None):
    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next
    return head
```

### Types of Linked Lists

There are three (3) types of linked lists:

1. Singly-linked lists
2. Doubly-linked lists
3. Circular lists

#### Singly Linked Lists

Each node in the list is connected only to the next node in the list (except the last one of course); in this sense, each node has a *value* and a *next* pointer, as such:

```Python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

To provide common linked list operations, we'd want to create a `LinkedList` class:

```Python
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return
   	def to_list(self) -> list:
        """
        Converts a linked list to list
        """
        node = self.head
        l = []
        while node:
            l.append(node.value)
            node = node.next
        return l
```

#### Doubly Linked Lists

All nodes in the list, except the *head* and *tail*, is connected to both the next node and the previous node. The *head* node is only connected to the next node, and the *tail* node is only connected to the previous node.

This type of list requires modifying our previously constituted Node class, so we can add another instance variable  that can be used to reference the *previous* node.

Translating it to code would look something like this:

```Python
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
```

Our `LinkedList` class is a bit different now, as we can use the new Node instance variable to speed up our traversal operations, specifically our *append* method that adds to the tail of the list:

```Python
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        self.tail.next = DoubleNode(value)
    	self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return
```

#### Circular LinkedLists

A `LinkedList` is circular when one of the nodes link back to another node in the chain. It is considered pathological because of the risk of an infinite traversal. The only way to avoid it is by detecting when a loop occurs.

### Some LinkedList Operations

#### Reversing a LinkedList

The gist is to traverse the old list while prepending to the new list and updating the Head reference in each operation. 

The algorithm could look something like this:

1. Start with the head of your old LinkedList (`current_node = old_list.head`)
2. Make a new LinkedList to store the reversed list (`new_list = LinkedList()`)
3. Assign a new node instance of `old_list.head.value` to `new_list.head`
4. Traverse `old_list` by assigning `current_node.next` to `current_node`, until `current_node` is `None`.
5. In each iteration, create a new `Node` with `current_node.value`
6. Assign `new_list.head.next` to the new `Node` instance of `current_node` and assign `new_list.head` to `new_list.head.next`

#### Detecting a Loop inside a LinkedList

The idea is to traverse the list at two different speeds: 

* One node at a time => slow runner
* Two nodes at a time => fast runner

We can detect a loop if:
* the next node refers back itself
* if the fast runner and slow runner refer to the same Node instance

And we can know there isn't a loop if:
* The fast runner reaches the end of the list

The algorithm:
1. Assign `LinkedList.head` to `fast_runner` and `slow_runner`
2. While `fast_runner.next` or `fast_runner.next.next` is not None, do step three (3), four (4) and five (5).
3. Return False if `slow_runner.next` refer to the same Node instance as `slow_runner`
4. Assign `slow_runner.next` to `slow_runner` and `fast_runner.next.next` to `fast_runner`
5. Return True is `slow_runner` refer to the same Node instance as `fast_runner`
6. Return False when the while loop is done

The code:
```python
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
```

