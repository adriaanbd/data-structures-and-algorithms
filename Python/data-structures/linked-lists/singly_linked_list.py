from node import Node


class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for val in init_list:
                self.append(val)
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])
