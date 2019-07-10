class Heap:
    def __init__(self, init_len):
        self.array = [None for _ in range(init_len)]
        self.next_idx = 0
        self.max = init_len

    def insert(self, data):
        self.array[self.next_idx] = data
        self.next_idx += 1

        if self.next_idx == self.max:
            self._handle_max_capacity()

    def _handle_max_capacity(self):
        self.array += [None for _ in range(self.max)]
        self.max *= 2
