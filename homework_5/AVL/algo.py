class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    @staticmethod
    def _height(node):
        return node.height if node is not None else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _balance(self, node):
        self._update_height(node)
        factor = self._balance_factor(node)
        if factor > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if factor < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def insert(self, value):
        def add(node):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = add(node.left)
            elif value > node.value:
                node.right = add(node.right)
            else:
                return node
            return self._balance(node)

        self.root = add(self.root)

    def delete(self, value):
        def remove(node, key):
            if node is None:
                return None
            if key < node.value:
                node.left = remove(node.left, key)
            elif key > node.value:
                node.right = remove(node.right, key)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                successor = node.right
                while successor.left is not None:
                    successor = successor.left
                node.value = successor.value
                node.right = remove(node.right, successor.value)
            return self._balance(node)

        self.root = remove(self.root, value)

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def inorder(self):
        result = []

        def visit(node):
            if node is None:
                return
            visit(node.left)
            result.append(node.value)
            visit(node.right)

        visit(self.root)
        return result
