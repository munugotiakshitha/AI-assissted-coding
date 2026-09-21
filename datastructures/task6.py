from collections import deque


class DequeDS:
    """Double-ended queue implementation."""

    def __init__(self):
        self.items = deque()

    def insert_front(self, item):
        """Insert an item at the front."""
        self.items.appendleft(item)

    def insert_rear(self, item):
        """Insert an item at the rear."""
        self.items.append(item)

    def remove_front(self):
        """Remove an item from the front."""
        if not self.items:
            return "Deque is empty"
        return self.items.popleft()

    def remove_rear(self):
        """Remove an item from the rear."""
        if not self.items:
            return "Deque is empty"
        return self.items.pop()


d = DequeDS()

d.insert_front(10)
d.insert_rear(20)
d.insert_front(5)

print("Deque:", d.items)
print("Removed front:", d.remove_front())
print("Removed rear:", d.remove_rear())

#output
# Deque: deque([5, 10, 20])
# Removed front: 5
# Removed rear: 20