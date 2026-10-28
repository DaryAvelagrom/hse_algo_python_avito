import pytest

from homework_4.Binary_Tree.algo import (
    BinarySearchTree,
    Node,
    is_balanced,
    validate_bst,
)


TRAVERSALS = [
    ("preorder", [8, 3, 1, 6, 4, 7, 10, 14, 13]),
    ("inorder", [1, 3, 4, 6, 7, 8, 10, 13, 14]),
    ("postorder", [1, 4, 7, 6, 3, 13, 14, 10, 8]),
    ("reverse_preorder", [8, 10, 14, 13, 3, 6, 7, 4, 1]),
    ("reverse_inorder", [14, 13, 10, 8, 7, 6, 4, 3, 1]),
    ("reverse_postorder", [13, 14, 10, 7, 4, 6, 1, 3, 8]),
]


@pytest.mark.parametrize("method, expected", TRAVERSALS)
def test_traversal_example(method, expected):
    tree = BinarySearchTree()
    for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        tree.insert(value)
    assert getattr(tree, method)() == expected
    assert getattr(tree, method)() == expected
    assert validate_bst(tree.root)


@pytest.mark.parametrize("method, expected", TRAVERSALS)
@pytest.mark.parametrize("values", [[], [0]])
def test_empty_and_single_node_traversals(method, expected, values):
    tree = BinarySearchTree()
    for value in values:
        tree.insert(value)
    assert getattr(tree, method)() == values


@pytest.mark.parametrize(
    "values",
    [list(range(30)), list(range(30, -1, -1)), [0, -5, 9, -10, -2, 3],
     [5, 5, 3, 3, 8, 8, 5]],
)
def test_insert(values):
    tree = BinarySearchTree()
    for value in values:
        tree.insert(value)
        assert validate_bst(tree.root)
    assert tree.inorder() == sorted(set(values))
    assert tree.reverse_inorder() == sorted(set(values), reverse=True)


@pytest.mark.parametrize(
    "root, expected",
    [
        (None, True),
        (Node(0), True),
        (Node(2, Node(1), Node(3)), True),
        (Node(0, Node(-10, None, Node(-1)), Node(10)), True),
        (Node(10**100, Node(-(10**100))), True),
        (Node(2, Node(3)), False),
        (Node(2, None, Node(1)), False),
        (Node(2, Node(2)), False),
        (Node(2, None, Node(2)), False),
        (Node(10, Node(5, None, Node(12)), Node(15)), False),
        (Node(10, Node(5), Node(15, Node(6))), False),
        (Node(10, Node(5, None, Node(10))), False),
    ],
)
def test_validate_bst(root, expected):
    assert validate_bst(root) is expected


@pytest.mark.parametrize(
    "root, expected",
    [
        (None, True),
        (Node(1), True),
        (Node(1, Node(2)), True),
        (Node(1, None, Node(2)), True),
        (Node(1, Node(2), Node(3)), True),
        (Node(1, Node(2, Node(4)), Node(3)), True),
        (Node(1, Node(2, Node(3))), False),
        (Node(1, None, Node(2, None, Node(3))), False),
        # At the root the heights differ by 1, but the left subtree is unbalanced.
        (Node(1, Node(2, Node(3, Node(4))), Node(5, None, Node(6))), False),
        (Node(1, Node(2, Node(3)), Node(4, None, Node(5, None, Node(6)))), False),
    ],
)
def test_is_balanced(root, expected):
    assert is_balanced(root) is expected
