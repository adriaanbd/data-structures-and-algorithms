class Stack:
    """
    Stack implementation using an Array
    """
    def __init__(self, max_size=10):
        self.arr = [0 for _ in range(max_size)]
        self.next_idx = 0
        self.num_elems = 0

    def push(self, data):
        if self.next_idx == self.max_size:
            self._handle_stack_overflow()
        self.arr[self.num_elems] = data
        self.next_idx += 1
        self.num_elems += 1

    def pop(self):
        if self.is_empty():
            return None
        self.next_idx -= 1
        self.num_elems -= 1
        item = self.arr[self.next_idx]
        self.arr[self.next_idx] = 0
        return item

    def size(self):
        return self.max_size

    def is_empty(self):
        return self.num_elems == 0

    def _handle_stack_overflow(self):
        old_arr = self.arr[:]
        self.max_size *= 2
        self.arr = [0 for _ in range(self.max_size)]
        for idx, elem in enumerate(old_arr):
            self.arr[idx] = elem
