class Stack:
    def __init__(self):
        self.items = list()
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        self.items.pop()