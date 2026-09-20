import pytest

from stack_vs_queue.algo import Fifo, LinkedList, Lifo


@pytest.mark.parametrize(
    "operation",
    ["pop_head", "pop_tail", "peek_head", "peek_tail"],
)
def test_empty_linked_list_raises(operation):
    linked_list = LinkedList()

    with pytest.raises(IndexError):
        getattr(linked_list, operation)()


@pytest.mark.parametrize(
    "value, operation",
    [
        (1, "pop_head"),
        (1, "pop_tail"),
        ("value", "pop_head"),
        ("value", "pop_tail"),
    ],
)
def test_single_element(value, operation):
    linked_list = LinkedList()
    linked_list.push(value)

    assert linked_list.peek_head() == value
    assert linked_list.peek_tail() == value
    assert getattr(linked_list, operation)() == value


@pytest.mark.parametrize(
    "structure, values, expected",
    [
        (Lifo, [1, 2, 3], [3, 2, 1]),
        (Fifo, [1, 2, 3], [1, 2, 3]),
        (Lifo, [1], [1]),
        (Fifo, [1], [1]),
    ],
)
def test_stack_and_queue_order(structure, values, expected):
    container = structure()

    for value in values:
        container.push(value)

    assert container.peek() == expected[0]
    assert [container.pop() for _ in values] == expected


@pytest.mark.parametrize(
    "structure",
    [Lifo, Fifo],
)
def test_empty_stack_and_queue_raise(structure):
    container = structure()

    with pytest.raises(IndexError):
        container.pop()

    with pytest.raises(IndexError):
        container.peek()


@pytest.mark.parametrize(
    "structure, values, expected_peek",
    [
        (Lifo, [1, 2], 2),
        (Fifo, [1, 2], 1),
    ],
)
def test_peek_does_not_remove_element(structure, values, expected_peek):
    container = structure()

    for value in values:
        container.push(value)

    assert container.peek() == expected_peek
    assert container.peek() == expected_peek


@pytest.mark.parametrize(
    "structure, operations, expected",
    [
        (
            Lifo,
            [("push", 1), ("push", 2), ("pop", None),
             ("push", 3), ("push", 4)],
            [2, 4, 3, 1],
        ),
        (
            Fifo,
            [("push", 1), ("push", 2), ("pop", None),
             ("push", 3), ("push", 4)],
            [1, 2, 3, 4],
        ),
    ],
)
def test_mixed_operations(structure, operations, expected):
    container = structure()
    result = []

    for operation, value in operations:
        if operation == "push":
            container.push(value)
        else:
            result.append(container.pop())

    while True:
        try:
            result.append(container.pop())
        except IndexError:
            break

    assert result == expected


@pytest.mark.parametrize(
    "structure",
    [Lifo, Fifo],
)
def test_reuse_after_empty(structure):
    container = structure()

    container.push(1)
    assert container.pop() == 1

    container.push(2)

    assert container.peek() == 2
    assert container.pop() == 2


@pytest.mark.parametrize(
    "structure, expected",
    [
        (Lifo, list(reversed(range(1000)))),
        (Fifo, list(range(1000))),
    ],
)
def test_large_sequence(structure, expected):
    container = structure()

    for value in range(1000):
        container.push(value)

    result = [container.pop() for _ in range(1000)]

    assert result == expected