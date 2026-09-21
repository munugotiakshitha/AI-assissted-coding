class Node:
    """Represents a node in the BST."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    """Binary Search Tree implementation."""

    def __init__(self):
        self.root = None

    def insert(self, root, data):
        """Insert data recursively into the BST."""
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root

    def inorder(self, root):
        """Perform in-order traversal."""
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


tree = BST()

for value in [50, 30, 70, 20, 40, 60, 80]:
    tree.root = tree.insert(tree.root, value)

print("In-order traversal:")
tree.inorder(tree.root)

#output
# In-order traversal:
# 20 30 40 50 60 70 80
