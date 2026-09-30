import pytest

from homework_3.hash_table.algo import HashTable


@pytest.mark.parametrize(
    "operation",
    ["get", "remove"],
)
def test_empty_hash_table(operation):
    table = HashTable()

    assert len(table) == 0

    with pytest.raises(KeyError):
        getattr(table, operation)("missing")


@pytest.mark.parametrize(
    "key, value",
    [
        ("a", 1),
        (0, 0),
        (-1, "value"),
    ],
)
def test_insert_into_empty_hash_table(key, value):
    table = HashTable()

    table.insert(key, value)

    assert len(table) == 1
    assert table.get(key) == value


@pytest.mark.parametrize(
    "capacity, count",
    [
        (1, 10),
        (2, 20),
        (4, 100),
    ],
)
def test_resize_on_overflow(capacity, count):
    table = HashTable(capacity=capacity)

    old_capacity = table.capacity

    for i in range(count):
        table.insert(i, i * 10)

    assert table.capacity > old_capacity
    assert len(table) == count

    for i in range(count):
        assert table.get(i) == i * 10


@pytest.mark.parametrize(
    "capacity",
    [1, 2, 4],
)
def test_values_are_not_lost_after_resize(capacity):
    table = HashTable(capacity=capacity)

    values = [
        ("a", 1),
        ("b", 2),
        ("c", 3),
        ("d", 4),
        ("e", 5),
    ]

    for key, value in values:
        table.insert(key, value)

    for key, value in values:
        assert table.get(key) == value


@pytest.mark.parametrize(
    "count",
    [2, 5, 20],
)
def test_collision(count):
    class SameHash:
        def __init__(self, value):
            self.value = value

        def __hash__(self):
            return 1

        def __eq__(self, other):
            return (
                isinstance(other, SameHash)
                and self.value == other.value
            )

    table = HashTable()
    keys = [SameHash(i) for i in range(count)]

    for i, key in enumerate(keys):
        table.insert(key, i)

    assert len(table) == count

    for i, key in enumerate(keys):
        assert table.get(key) == i


@pytest.mark.parametrize(
    "removed_index",
    [0, 1, 2],
)
def test_remove_element_from_collision_bucket(removed_index):
    class SameHash:
        def __init__(self, value):
            self.value = value

        def __hash__(self):
            return 1

        def __eq__(self, other):
            return (
                isinstance(other, SameHash)
                and self.value == other.value
            )

    table = HashTable()

    keys = [
        SameHash("a"),
        SameHash("b"),
        SameHash("c"),
    ]

    for i, key in enumerate(keys):
        table.insert(key, i)

    table.remove(keys[removed_index])

    assert keys[removed_index] not in table
    assert len(table) == 2

    for i, key in enumerate(keys):
        if i != removed_index:
            assert table.get(key) == i


def test_update_value_with_collision():
    class SameHash:
        def __init__(self, value):
            self.value = value

        def __hash__(self):
            return 1

        def __eq__(self, other):
            return (
                isinstance(other, SameHash)
                and self.value == other.value
            )

    table = HashTable()

    key1 = SameHash("a")
    key2 = SameHash("b")

    table.insert(key1, 1)
    table.insert(key2, 2)

    table.insert(key1, 100)

    assert table.get(key1) == 100
    assert table.get(key2) == 2
    assert len(table) == 2


def test_collision_survives_resize():
    class SameHash:
        def __init__(self, value):
            self.value = value

        def __hash__(self):
            return 1

        def __eq__(self, other):
            return (
                isinstance(other, SameHash)
                and self.value == other.value
            )

    table = HashTable(capacity=2)

    keys = [SameHash(i) for i in range(20)]

    for i, key in enumerate(keys):
        table.insert(key, i)

    assert table.capacity > 2

    for i, key in enumerate(keys):
        assert table.get(key) == i


def test_remove_all_elements():
    table = HashTable()

    for i in range(10):
        table.insert(i, i)

    for i in range(10):
        assert table.remove(i) == i

    assert len(table) == 0

    for i in range(10):
        assert i not in table


def test_reuse_after_becoming_empty():
    table = HashTable()

    table.insert("a", 1)
    table.remove("a")

    assert len(table) == 0

    table.insert("b", 2)

    assert len(table) == 1
    assert table.get("b") == 2