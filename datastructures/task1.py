class Stack:
    """A simple Stack implementation using a Python list."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        """Check whether the stack is empty."""
        return len(self.items) == 0


# Example
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Top:", s.peek())
print("Removed:", s.pop())
print("Stack empty:", s.is_empty())

#output
# Top: 30
# Removed: 30
# Stack empty: False