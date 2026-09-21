# #TABLE
# #| Feature                     | Data Structure     | Justification                                                                                                                               |
# | --------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
# | Student Attendance Tracking | **Stack**          | A stack can maintain the most recently recorded entry/exit information. The latest record can be accessed first.                            |
# | Event Registration          | **Hash Table**     | A hash table provides fast lookup using a student's ID or registration ID. It also makes removal efficient.                                 |
# | Library Book Borrowing      | **Priority Queue** | Books or borrowing requests can be organized according to due dates or priority. The item with the highest priority can be processed first. |
# | Bus Scheduling              | **Graph**          | A graph can represent bus stops as vertices and connections between stops as edges.                                                         |
# | Cafeteria Order Queue       | **Queue**          | Students' orders should be served in the same order they arrive, which follows FIFO.                                                        |

class CafeteriaQueue:
    """Queue for processing cafeteria orders."""

    def __init__(self):
        self.orders = []

    def add_order(self, order):
        """Add a new order to the queue."""
        self.orders.append(order)

    def serve_order(self):
        """Serve the first order in the queue."""
        if not self.orders:
            return "No orders available"

        return self.orders.pop(0)

    def display_orders(self):
        """Display all pending orders."""
        print(self.orders)


cafeteria = CafeteriaQueue()

cafeteria.add_order("Burger")
cafeteria.add_order("Pizza")
cafeteria.add_order("Sandwich")

print("Pending orders:")
cafeteria.display_orders()

print("Serving:", cafeteria.serve_order())

print("Remaining orders:")
cafeteria.display_orders()

#output
#Pending orders:
# ['Burger', 'Pizza', 'Sandwich']

# Serving: Burger

# Remaining orders:
# ['Pizza', 'Sandwich']
