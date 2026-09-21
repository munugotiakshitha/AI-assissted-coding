# #TABLE
# #| Feature                  | Data Structure     | Justification                                                                                               |
# | ------------------------ | ------------------ | ----------------------------------------------------------------------------------------------------------- |
# | Shopping Cart Management | **Deque**          | A deque allows products to be added or removed from either end efficiently.                                 |
# | Order Processing         | **Queue**          | Orders need to be processed in the order they were placed, so FIFO is suitable.                             |
# | Top-Selling Products     | **Priority Queue** | Products can be prioritized according to their sales count so highly ranked products can be accessed first. |
# | Product Search Engine    | **BST**            | A BST can organize products by product ID and support searching based on the ID.                            |
# | Delivery Route Planning  | **Graph**          | Warehouses and delivery locations can be represented as vertices connected by routes/edges.                 |

class OrderQueue:
    """Queue for processing e-commerce orders."""

    def __init__(self):
        self.orders = []

    def add_order(self, order):
        """Add an order to the queue."""
        self.orders.append(order)

    def process_order(self):
        """Process the oldest order."""
        if not self.orders:
            return "No orders available"

        return self.orders.pop(0)

    def display_orders(self):
        """Display all pending orders."""
        print(self.orders)


orders = OrderQueue()

orders.add_order("Order 101")
orders.add_order("Order 102")
orders.add_order("Order 103")

print("Pending orders:")
orders.display_orders()

print("Processing:", orders.process_order())

print("Remaining orders:")
orders.display_orders()

# output
# Pending orders:
# ['Order 101', 'Order 102', 'Order 103']

# Processing: Order 101

# Remaining orders:
# ['Order 102', 'Order 103']
