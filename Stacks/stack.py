class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return None if self.is_empty() else self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return None if self.is_empty() else self.items[-1]

    def get_items(self):
        return self.items
