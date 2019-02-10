class Node:
    def __init__(self, data=None, next_node=None):
        self._data = data 
        self._next = next_node
    
    @property
    def data(self):
        return self._data
    
    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node


n1 = Node(1)
assert n1.data == 1
n2 = Node(2)
assert n2.data == 2
n1.next = n2
assert n1.next.data == 2

