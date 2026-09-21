import heapq


class PriorityQueue:
    """Priority Queue using Python heapq."""

    def __init__(self):
        self.items = []

    def enqueue(self, item, priority):
        """Add an item with a priority."""
        heapq.heappush(self.items, (priority, item))

    def dequeue(self):
        """Remove the highest-priority item."""
        if not self.items:
            return "Priority Queue is empty"

        priority, item = heapq.heappop(self.items)
        return item

    def display(self):
        """Display the priority queue."""
        print(self.items)


pq = PriorityQueue()

pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)

print("Queue:")
pq.display()

print("Removed:", pq.dequeue())

#output
# Queue:
# [(1, 'Task B'), (3, 'Task A'), (2, 'Task C')]
# Removed: Task B