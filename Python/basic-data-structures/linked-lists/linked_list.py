from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node
        self.length += 1

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

    def search(self, value):
        """ Search the linked list for a node with the requested value
        and return the node. """
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        raise ValueError(f"{value} not found!")

    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head.value == value:
            if self.length == 1:
                self.head = None
                self.tail = self.head
            else:
                self.head = self.head.next
            self.length -= 1
            return
        node = self.head
        while node:
            if node.next.value == value:
                if self.tail == node.next:
                    self.tail = node
                    self.tail.next = None
                else:
                    node.next = node.next.next
                self.length -= 1
                return
            node = node.next
        raise ValueError(f"{value} not found!")

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            raise IndexError("Can't pop from empty list!")
        elif self.length == 1:
            node = self.head
            self.head = None
            self.tail = self.head
        elif self.length == 2:
            node = self.head
            self.head = self.tail
        else:
            node = self.head
            self.head = self.head.next
        self.length -= 1
        return node.value

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
