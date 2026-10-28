class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value == current.value:
                return
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    def _traverse(self, order, reverse=False):
        result = []

        def visit(node):
            if node is None:
                return
            first, second = node.left, node.right
            if reverse:
                first, second = second, first
            if order == "pre":
                result.append(node.value)
            visit(first)
            if order == "in":
                result.append(node.value)
            visit(second)
            if order == "post":
                result.append(node.value)

        visit(self.root)
        return result

    def preorder(self):
        return self._traverse("pre")

    def inorder(self):
        return self._traverse("in")

    def postorder(self):
        return self._traverse("post")

    def reverse_preorder(self):
        return self._traverse("pre", reverse=True)

    def reverse_inorder(self):
        return self._traverse("in", reverse=True)

    def reverse_postorder(self):
        return self._traverse("post", reverse=True)


def validate_bst(root):
    def check(node, lower, upper):
        if node is None:
            return True
        if lower is not None and node.value <= lower:
            return False
        if upper is not None and node.value >= upper:
            return False
        return (
            check(node.left, lower, node.value)
            and check(node.right, node.value, upper)
        )

    return check(root, None, None)


def is_balanced(root):
    def height(node):
        if node is None:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return height(root) != -1
