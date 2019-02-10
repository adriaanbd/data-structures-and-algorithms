class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_back(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next_pointer = node
        self.tail = node
        self.size += 1

    def add_front(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next_pointer = self.head
        self.head = node
        self.size += 1

    def get(self, index):
        if index > self.size - 1:
            raise IndexError
        elif index == 0:
            return self.head.key
        elif index == self.size:
            return self.tail.key
        current_node = self.head.next_pointer
        for i in range(index - 1):
            current_node = current_node.next_pointer
        return current_node.key

