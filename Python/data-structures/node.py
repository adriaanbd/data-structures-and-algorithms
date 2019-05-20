class Node:
    def __init__(self, key):
        self._key = key
        self._next = None

    @property
    def key(self):
        return self._key

    @property
    def next_pointer(self):
        return self._next

    @next_pointer.setter
    def next_pointer(self, node):
        self._next = node
