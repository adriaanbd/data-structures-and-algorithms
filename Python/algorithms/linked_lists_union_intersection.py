class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.length = 0
        if iterable:
            self.create_from(iterable)

    def append(self, value):
        """ Append a value to the end of the list. """
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if pos >= self.length - 1:
            self.append(value)
            return
        elif pos == 0:
            self.prepend(value)
            return
        elif pos == 1:
            node = Node(value)
            node.next = self.head.next
            self.head.next = node
            self.head.next
        else:
            current_node = self.head
            new_node = Node(value)
            for _ in range(pos - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
        self.length += 1
        return

    def size(self):
        """ Return the size or length of the linked list. """
        return self.length

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def create_from(self, iterable):
        for value in iterable:
            if self.head is None:
                self.head = Node(value)
                self.tail = self.head
            else:
                current = self.tail
                current.next = Node(value)
                self.tail = current.next
        return self.head

    def __str__(self):
        current_node = self.head
        out_string = ""
        while current_node:
            out_string += str(current_node.value) + "->"
            current_node = current_node.next
        return f"HEAD->" + out_string + "TAIL"


def union(llist_one, llist_two):
    set_one = set(llist_one.to_list())
    set_two = set(llist_two.to_list())
    out = set_one | set_two
    llist = LinkedList(out)

    return llist


def intersection(llist_one, llist_two):
    set_one = set(llist_one.to_list())
    set_two = set(llist_two.to_list())
    out = set_one & set_two
    llist = LinkedList(out)

    return llist


llist_one = LinkedList()
llist_two = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    llist_one.append(i)

for i in element_2:
    llist_two.append(i)

print(union(llist_one, llist_two))
print(intersection(llist_one, llist_two))

# Test case 2

llist_3 = LinkedList()
llist_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    llist_3.append(i)

for i in element_2:
    llist_4.append(i)

print(union(llist_3, llist_4))
print(intersection(llist_3, llist_4))