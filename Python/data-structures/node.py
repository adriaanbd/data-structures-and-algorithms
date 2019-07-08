class Node:
    def __init__(self, key):
        self._key = key
        self._next = None

    @property
    def key(self):
        return self._key

    @property
    def next(self):
        return self._next

    @next.setter
    def next_pointer(self, node):
        self._next = node

    def __repr__(self):
        return str(self.key)
