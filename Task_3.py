# Write an algorithm (function) that finds the sum of all values in a binary search tree or AVL tree. Take any tree implementation from the notes or another source.

class AVLTreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLTreeNode(key)
        elif key < node.val:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and key < node.left.val:
            return self.right_rotate(node)

        if balance < -1 and key > node.right.val:
            return self.left_rotate(node)

        if balance > 1 and key > node.left.val:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and key < node.right.val:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def sum_of_values(self):
        return self._sum_of_values(self.root)

    def _sum_of_values(self, node):
        if node is None:
            return 0
        return node.val + self._sum_of_values(node.left) + self._sum_of_values(node.right)


avl_tree = AVLTree()
avl_elements = [50, 30, 20, 40, 70, 60, 80]
for elem in avl_elements:
    avl_tree.insert(elem)

sum_values_avl = avl_tree.sum_of_values()
print(f"The sum of all values in the AVL tree is: {sum_values_avl}")
