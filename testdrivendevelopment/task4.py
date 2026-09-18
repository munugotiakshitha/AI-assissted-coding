def run_tests():
	# Required test cases
	inv = Inventory()

	inv.add_item("Pen", 10)
	assert inv.get_stock("Pen") == 10

	inv.remove_item("Pen", 5)
	assert inv.get_stock("Pen") == 5

	inv.add_item("Book", 3)
	assert inv.get_stock("Book") == 3

	# Edge-case tests
	inv.add_item("Pen", 2)
	assert inv.get_stock("Pen") == 7

	assert inv.get_stock("Pencil") == 0

	inv.remove_item("Book", 10)
	assert inv.get_stock("Book") == 0


class Inventory:
	def __init__(self):
		# Store each item name and its quantity in a dictionary.
		self.items = {}

	def add_item(self, name, quantity):
		# Add a new item or increase the quantity of an existing item.
		if name in self.items:
			self.items[name] += quantity
		else:
			self.items[name] = quantity

	def remove_item(self, name, quantity):
		# Reduce the stock, but never let it become negative.
		if name in self.items:
			self.items[name] = max(0, self.items[name] - quantity)

	def get_stock(self, name):
		# Return zero when the item is not in the inventory.
		return self.items.get(name, 0)


run_tests()
print("All Task 4 tests passed!")
