import pytest

from merge_lists.algo import LinkedList, merge_lists_tmp, merge_lists_no_tmp


MERGE_FUNCTIONS = [merge_lists_tmp, merge_lists_no_tmp]


def make_list(values):
    linked_list = LinkedList()
    for value in values:
        linked_list.push(value)
    return linked_list


def to_list(head):
    result = []
    current = head

    while current is not None:
        result.append(current.value)
        current = current.next

    return result


def get_nodes(linked_list):
    nodes = []
    current = linked_list.head

    while current is not None:
        nodes.append(current)
        current = current.next

    return nodes


@pytest.mark.parametrize("merge", MERGE_FUNCTIONS)
@pytest.mark.parametrize(
    "values1, values2, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([1], [2], [1, 2]),
        ([5], [5], [5, 5]),
        ([1, 2, 3], [10, 11, 12], [1, 2, 3, 10, 11, 12]),
        ([10, 11, 12], [1, 2, 3], [1, 2, 3, 10, 11, 12]),
        (
            [1, 1, 2, 4, 4],
            [1, 2, 2, 4, 5],
            [1, 1, 1, 2, 2, 2, 4, 4, 4, 5],
        ),
        ([-10, -3, 0, 7], [-8, -3, 2, 9], [-10, -8, -3, -3, 0, 2, 7, 9]),
        ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], list(range(1, 11))),
        ([1, 5], [2, 3, 4, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
    ],
)
def test_merge_values(merge, values1, values2, expected):
    list1 = make_list(values1)
    list2 = make_list(values2)

    head = merge(list1, list2)

    assert to_list(head) == expected
