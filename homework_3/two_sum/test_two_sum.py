import pytest

from homework_3.two_sum.algo import two_sum


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 3, 4, 10], 7, (1, 2)),
        ([5, 5, 1, 4], 10, (0, 1)),
        ([2, 7], 9, (0, 1)),
        ([0, 4, 3, 0], 0, (0, 3)),
        ([-3, 4, 3, 90], 0, (0, 2)),
        ([-5, -2, -8, -1], -10, (1, 2)),
        ([1, -2, 7, 5], 3, (1, 3)),
        ([10, 20, 30, 40, 50], 90, (3, 4)),
        ([8, 1, 6, 3, 9], 10, (1, 4)),
        ([1000000, -999999, 5, 8], 1, (0, 1)),
    ],
)
def test_two_sum(arr, k, expected):
    assert two_sum(arr, k) == expected


def test_two_sum_does_not_modify_input():
    arr = [4, 1, 9, 6]
    original = arr.copy()

    two_sum(arr, 10)

    assert arr == original


def test_two_sum_large_input():
    arr = list(range(100_000))
    k = 199_997

    assert two_sum(arr, k) == (99_998, 99_999)
