class Stack():
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n"
            s += "\n".join([str(item) for item in self.list[::-1]])
            s += "\n<bottom of stack>"
            return s

        else:
            return "<stack is empty>"
