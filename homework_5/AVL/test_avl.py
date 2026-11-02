import random

import pytest

from homework_5.AVL.algo import AVL


def check_tree(tree, expected):
    def check(node, lower=None, upper=None):
        if node is None:
            return 0
        assert lower is None or lower < node.value
        assert upper is None or node.value < upper
        left = check(node.left, lower, node.value)
        right = check(node.right, node.value, upper)
        assert abs(left - right) <= 1
        assert node.height == 1 + max(left, right)
        return node.height

    check(tree.root)
    assert tree.inorder() == sorted(expected)


@pytest.mark.parametrize("values", [
    [30, 20, 10], [10, 20, 30], [30, 10, 20], [10, 30, 20],
])
def test_four_insert_rotations(values):
    tree = AVL()
    for index, value in enumerate(values):
        tree.insert(value)
        check_tree(tree, set(values[:index + 1]))
    assert tree.root.value == 20
    assert tree.root.left.value == 10
    assert tree.root.right.value == 30


def test_empty_and_single_node():
    tree = AVL()
    check_tree(tree, set())
    assert tree.search(1) is False
    tree.delete(1)
    tree.insert(0)
    assert tree.search(0) is True
    check_tree(tree, {0})
    tree.insert(0)
    check_tree(tree, {0})
    tree.delete(0)
    tree.delete(0)
    assert tree.root is None
    assert tree.search(0) is False


@pytest.mark.parametrize("values, deleted", [
    ([2, 1, 3], 1),
    ([2, 1], 2),
    ([4, 2, 6, 5], 6),
    ([4, 2, 6, 1, 3, 5, 7], 4),
    ([8, 4, 12, 2, 6, 10, 14, 9, 11], 8),
    ([4, 2, 5, 1, 3], 5),
    ([2, 1, 4, 3, 5], 1),
    ([5, 2, 8, 1, 4, 7, 3], 7),
    ([5, 2, 8, 3, 6, 9, 7], 3),
    ([2, 1, 3], 99),
])
def test_delete_cases(values, deleted):
    tree = AVL()
    for value in values:
        tree.insert(value)
    tree.delete(deleted)
    check_tree(tree, set(values) - {deleted})
    assert tree.search(deleted) is False


@pytest.mark.parametrize("values", [
    list(range(200)), list(range(200, -1, -1)),
    [0, -5, 9, -10, -2, 3, 0, 9, 10**100, -(10**100)],
])
def test_insert_search_and_delete_all(values):
    tree = AVL()
    expected = set()
    for value in values:
        tree.insert(value)
        expected.add(value)
        check_tree(tree, expected)
        assert tree.search(value) is True
    for value in values:
        tree.delete(value)
        expected.discard(value)
        check_tree(tree, expected)
        assert tree.search(value) is False
    assert tree.root is None


def test_mixed_operations():
    randomizer = random.Random(42)
    tree = AVL()
    expected = set()
    for _ in range(1000):
        value = randomizer.randrange(-100, 101)
        if randomizer.choice([True, False]):
            tree.insert(value)
            expected.add(value)
        else:
            tree.delete(value)
            expected.discard(value)
        check_tree(tree, expected)
        assert tree.search(value) is (value in expected)
