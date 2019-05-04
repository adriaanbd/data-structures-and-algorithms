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

