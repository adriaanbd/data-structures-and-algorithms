class Node:
    def __init__(self, key):
        self._key = key
        self._next_pointer = None

    @property
    def key(self):
        return self._key

    @property
    def next_pointer(self):
        return self._next_pointer

    @next_pointer.setter
    def next_pointer(self, node):
        self._next_pointer = node
