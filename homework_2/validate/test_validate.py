import pytest

from validate.algo import validate


@pytest.mark.parametrize(
    "pushed, popped, expected",
    [
        ([1], [1], True),
        ([1, 2, 3, 4, 5], [1, 3, 5, 4, 2], True),
        ([1, 2, 3], [3, 1, 2], False),
        ([1, 2, 3], [3, 2, 1], True),
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2, 3, 4], [2, 1, 4, 3], True),
        ([1, 2, 3, 4], [2, 4, 1, 3], False),
        ([0, -1, 2], [0, 2, -1], True),
        ([-3, -2, -1, 0], [0, -1, -2, -3], True),
        ([10, 20, 30, 40, 50], [30, 20, 50, 40, 10], True),
        ([10, 20, 30, 40, 50], [30, 10, 20, 50, 40], False),
    ],
)
def test_validate(pushed, popped, expected):
    assert validate(pushed, popped) == expected